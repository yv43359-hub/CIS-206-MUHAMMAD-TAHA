import csv
import os


# Function to load customer information from the CSV file
def load_customers(filename):
    """Read customer records from a CSV file into a list of dictionaries."""
    customers = []

    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                customers.append(row)

    except FileNotFoundError:
        print("Error: customers.csv was not found.")
        print("Please place customers.csv in the same folder as this program.")

    except Exception as error:
        print("Error reading the file:", error)

    return customers


# Function to display customer information
def display_customers(customers, sort_field):
    """Display customer names, company names, and phone numbers."""
    if not customers:
        print("No customer records available.")
        return

    sorted_customers = sorted(
        customers,
        key=lambda customer: customer.get(sort_field, "").lower()
    )

    for customer in sorted_customers:
        company = customer.get("CompanyName", "")
        contact = customer.get("ContactName", "")
        phone = customer.get("Phone", "")

        print(f"Company Name: {company}")
        print(f"Contact Name: {contact}")
        print(f"Phone Number: {phone}")
        print("-" * 40)


# Function to search for customers
def search_customers(customers, field, search_text):
    """Search customer records by company name or contact name."""
    if not search_text.strip():
        print("Please enter a search term.")
        return

    found = False
    search_text = search_text.strip().lower()

    for customer in customers:
        value = customer.get(field, "")

        if search_text in value.lower():
            print(f"Company Name: {customer.get('CompanyName', '')}")
            print(f"Contact Name: {customer.get('ContactName', '')}")
            print(f"Phone Number: {customer.get('Phone', '')}")
            print("-" * 40)
            found = True

    if not found:
        print("No matching customers found.")


# Function to display the program menu
def display_menu():
    """Display the available options."""
    print("\nCustomer Information System")
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search by company name")
    print("4. Search by contact name")
    print("5. Exit")


# Main function to run the program
def main():
    """Load customer data and allow the user to choose an operation."""
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NorthwindCustomers.csv")
    customers = load_customers(filename)

    if not customers:
        print("No customer records loaded. Please check the CSV file.")
        return

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_customers(customers, "CompanyName")

        elif choice == "2":
            display_customers(customers, "ContactName")

        elif choice == "3":
            company_name = input("Enter a company name or part of a name: ")
            search_customers(customers, "CompanyName", company_name)

        elif choice == "4":
            contact_name = input("Enter a contact name or part of a name: ")
            search_customers(customers, "ContactName", contact_name)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()