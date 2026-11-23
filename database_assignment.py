
import sqlite3

# Connect to the Northwind database
DATABASE_NAME = "northwind.db"


# Get a connection to the database
def connect_database():
    return sqlite3.connect(DATABASE_NAME)


# Get all table names from the database
def get_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]
    return tables


# Display all records in a selected table
def display_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM "{table_name}"')
    records = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    # Determine the width of each column
    widths = []
    for index, column in enumerate(columns):
        max_width = len(column)
        for record in records:
            value_length = len(str(record[index])) if record[index] is not None else 4
            max_width = max(max_width, value_length)
        widths.append(max_width)

    # Display column headings
    print("\n" + "-" * 80)
    heading = " | ".join(columns[i].ljust(widths[i]) for i in range(len(columns)))
    print(heading)
    print("-" * len(heading))

    # Display the records with row numbers
    for row_number, record in enumerate(records, start=1):
        formatted_row = []
        for index, value in enumerate(record):
            text = str(value) if value is not None else "NULL"
            formatted_row.append(text.ljust(widths[index]))
        print(f"{row_number}. " + " | ".join(formatted_row))

    print(f"\nTotal records: {len(records)}")
    return records, columns


# Allow the user to select a table from a list
def select_table(tables):
    print("\nAvailable Tables:")
    for number, table in enumerate(tables, start=1):
        print(f"{number}. {table}")

    while True:
        try:
            choice = int(input("Select a table number: "))
            if 1 <= choice <= len(tables):
                return tables[choice - 1]
            print("Invalid selection. Please choose a listed number.")
        except ValueError:
            print("Please enter a valid number.")


# Get table columns and primary key information
def get_table_info(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f'PRAGMA table_info("{table_name}")')
    return cursor.fetchall()


# Insert a new record into a selected table
def insert_record(connection, table_name):
    table_info = get_table_info(connection, table_name)
    columns = [column[1] for column in table_info]

    values = []
    print("\nEnter values for the new record.")
    print("Press Enter without typing anything to leave a field blank.")

    for column in columns:
        value = input(f"{column}: ")
        values.append(value if value != "" else None)

    placeholders = ", ".join(["?"] * len(columns))
    column_names = ", ".join(f'"{column}"' for column in columns)

    cursor = connection.cursor()
    cursor.execute(
        f'INSERT INTO "{table_name}" ({column_names}) VALUES ({placeholders})',
        values
    )
    connection.commit()
    print("Record inserted successfully.")


# Update a selected record in a table
def update_record(connection, table_name):
    table_info = get_table_info(connection, table_name)
    primary_keys = [column[1] for column in table_info if column[5] > 0]

    if not primary_keys:
        print("This table does not have a primary key.")
        return

    display_table(connection, table_name)

    # Select the record to update using its primary key
    key_column = primary_keys[0]
    key_value = input(f"\nEnter the {key_column} of the record to update: ")

    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM "{table_name}" WHERE "{key_column}" = ?', (key_value,))
    record = cursor.fetchone()

    if record is None:
        print("Record not found.")
        return

    columns = [description[0] for description in cursor.description]

    # Display fields available for updating
    print("\nFields:")
    for number, column in enumerate(columns, start=1):
        print(f"{number}. {column}")

    try:
        field_choice = int(input("Select the field number to update: "))
        if not 1 <= field_choice <= len(columns):
            print("Invalid field selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    selected_column = columns[field_choice - 1]
    new_value = input(f"Enter the new value for {selected_column}: ")

    cursor.execute(
        f'UPDATE "{table_name}" SET "{selected_column}" = ? WHERE "{key_column}" = ?',
        (new_value, key_value)
    )
    connection.commit()
    print("Record updated successfully.")


# Delete a selected record from a table
def delete_record(connection, table_name):
    table_info = get_table_info(connection, table_name)
    primary_keys = [column[1] for column in table_info if column[5] > 0]

    if not primary_keys:
        print("This table does not have a primary key.")
        return

    display_table(connection, table_name)

    # Select the record to delete using its primary key
    key_column = primary_keys[0]
    key_value = input(f"\nEnter the {key_column} of the record to delete: ")

    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM "{table_name}" WHERE "{key_column}" = ?', (key_value,))
    record = cursor.fetchone()

    if record is None:
        print("Record not found.")
        return

    # Confirm before deleting the record
    confirm = input("Are you sure you want to delete this record? (Y/N): ").strip().upper()

    if confirm == "Y":
        cursor.execute(
            f'DELETE FROM "{table_name}" WHERE "{key_column}" = ?',
            (key_value,)
        )
        connection.commit()
        print("Record deleted successfully.")
    else:
        print("Delete canceled.")


# Display the insert, update, and delete menu
def modify_menu(connection, table_name):
    while True:
        print(f"\nModify Table: {table_name}")
        print("I. Insert a record")
        print("U. Update a record")
        print("D. Delete a record")
        print("V. View records")
        print("Q. Return to main menu")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "I":
            insert_record(connection, table_name)
        elif choice == "U":
            update_record(connection, table_name)
        elif choice == "D":
            delete_record(connection, table_name)
        elif choice == "V":
            display_table(connection, table_name)
        elif choice == "Q":
            break
        else:
            print("Invalid choice. Please try again.")


# Main program menu
def main():
    connection = connect_database()

    try:
        tables = get_tables(connection)

        if not tables:
            print("No tables found. Make sure the Northwind database has been created.")
            return

        # Main menu lets the user read tables or modify permitted tables
        while True:
            print("\n===== NORTHWIND DATABASE =====")
            print("1. Read a table")
            print("2. Modify a table")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                table_name = select_table(tables)
                display_table(connection, table_name)

            elif choice == "2":
                # Only customers, employees, and products may be modified
                allowed_tables = ["customers", "employees", "products"]
                available_tables = [
                    table for table in tables
                    if table.lower() in allowed_tables
                ]

                if not available_tables:
                    print("No permitted tables are available.")
                    continue

                table_name = select_table(available_tables)
                modify_menu(connection, table_name)

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1, 2, or 3.")

    finally:
        # Close the database connection when the program ends
        connection.close()


# Start the program
if __name__ == "__main__":
    main()
