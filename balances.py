"""
Balances class for the ATM system.

This class stores account balances and provides methods
to check and update balances.
"""


class Balances:
    """Manage checking and savings account balances."""

    def __init__(self, checking=0.0, savings=0.0):
        """Initialize account balances."""
        if not isinstance(checking, (int, float)) or not isinstance(savings, (int, float)):
            raise TypeError("Balances must be numbers.")

        if checking < 0 or savings < 0:
            raise ValueError("Balances cannot be negative.")

        self.checking = float(checking)
        self.savings = float(savings)

    def get_checking(self):
        """Return the checking account balance."""
        return self.checking

    def get_savings(self):
        """Return the savings account balance."""
        return self.savings

    def deposit_checking(self, amount):
        """Deposit money into checking."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")

        self.checking += amount

    def deposit_savings(self, amount):
        """Deposit money into savings."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")

        self.savings += amount

    def withdraw_checking(self, amount):
        """Withdraw money from checking."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")

        if amount > self.checking:
            raise ValueError("Insufficient checking balance.")

        self.checking -= amount

    def withdraw_savings(self, amount):
        """Withdraw money from savings."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")

        if amount > self.savings:
            raise ValueError("Insufficient savings balance.")

        self.savings -= amount

    def __str__(self):
        """Display both account balances."""
        return (
            f"Checking: ${self.checking:.2f}\n"
            f"Savings: ${self.savings:.2f}"
        )


# Test the Balances class
if __name__ == "__main__":
    accounts = Balances(1000, 500)

    print("Starting balances:")
    print(accounts)

    accounts.deposit_checking(200)
    accounts.deposit_savings(100)

    print("\nAfter deposits:")
    print(accounts)

    accounts.withdraw_checking(50)
    accounts.withdraw_savings(25)

    print("\nAfter withdrawals:")
    print(accounts)