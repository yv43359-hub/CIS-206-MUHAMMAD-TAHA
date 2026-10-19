
"""
CIS 206 - Session 8 Assignment
Read Northwind customer data and allow users to sort and search customers.
"""

import csv
import os


def load_customers(filename):
    """Read customer records from a CSV file into a list of dictionaries."""
    customers = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"CompanyName", "ContactName", "Phone"}
        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                "The CSV file must contain CompanyName, ContactName, and Phone columns."
            )

        for row in reader:
            customers.append(row)

    if not customers:
        raise ValueError("The customer file contains no customer records.")

    return customers


def display_customers(customers, sort_by):
    """Display customers sorted by company name or contact name."""
    if sort_by not in ("CompanyName", "ContactName"):
        raise ValueError("Invalid sorting field.")

    sorted_customers = sorted(
        customers,
        key=lambda customer: (customer.get(sort_by) or "").casefold()
    )

    for customer in sorted_customers:
        print("-" * 40)
        print("Company Name:", customer.get("CompanyName", ""))
        print("Contact Name:", customer.get("ContactName", ""))
        print("Phone:", customer.get("Phone", ""))

    print("-" * 40)
    print("Total customers:", len(sorted_customers))


def search_customers(customers, field):
    """Search customer records by a full or partial name."""
    if field not in ("CompanyName", "ContactName"):
        raise ValueError("Invalid search field.")

    search_term = input("Enter a full or partial name: ").strip()

    if not search_term:
        print("Search cannot be empty.")
        return

    matches = [
        customer for customer in customers
        if search_term.casefold() in
        (customer.get(field) or "").casefold()
    ]

    if matches:
        print("\nMatching customers:")
        for customer in matches:
            print("-" * 40)
            print("Company Name:", customer.get("CompanyName", ""))
            print("Contact Name:", customer.get("ContactName", ""))
            print("Phone:", customer.get("Phone", ""))
        print("-" * 40)
        print("Matches found:", len(matches))
    else:
        print("No matching customers found.")


def display_menu():
    """Display the main menu."""
    print("\nNORTHWIND CUSTOMER MENU")
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")


def main():
    """Load the data and run the customer menu."""
    filename = os.path.join(os.path.dirname(__file__), "NorthwindCustomers.csv")

    try:
        customers = load_customers(filename)
    except FileNotFoundError:
        print("Error: NorthwindCustomers.csv was not found.")
        print("Place the CSV file in the same folder as this Python program.")
        return
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print("Error reading customer data:", error)
        return

    print("Customer data loaded successfully.")
    print("Number of customers:", len(customers))

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_customers(customers, "CompanyName")
        elif choice == "2":
            display_customers(customers, "ContactName")
        elif choice == "3":
            search_customers(customers, "CompanyName")
        elif choice == "4":
            search_customers(customers, "ContactName")
        elif choice == "5":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
