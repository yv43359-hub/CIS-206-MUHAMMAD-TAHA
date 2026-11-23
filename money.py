"""
Money class for the ATM system.

This class stores and manages monetary amounts.
It validates amounts and supports adding and subtracting money.
"""


class Money:
    """Represent an amount of money."""

    def __init__(self, amount=0.0):
        """Initialize money with a valid non-negative amount."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        self.amount = float(amount)

    def add(self, amount):
        """Add money to the current amount."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.amount += amount

    def subtract(self, amount):
        """Subtract money if sufficient funds are available."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > self.amount:
            raise ValueError("Insufficient funds.")

        self.amount -= amount

    def get_amount(self):
        """Return the current amount."""
        return self.amount

    def __str__(self):
        """Return the amount formatted as currency."""
        return f"${self.amount:.2f}"


# Test the Money class
if __name__ == "__main__":
    wallet = Money(100)

    print("Starting balance:", wallet)

    wallet.add(50)
    print("After deposit:", wallet)

    wallet.subtract(25)
    print("After withdrawal:", wallet)