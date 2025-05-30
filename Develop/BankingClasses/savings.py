"""The savings account class."""
# TODO: Import the BankAccount class from the banking file.
from .banking import BankAccount

# TODO: Implement the SavingsAccount class, which inherits from the BankAccount class.
class SavingsAccount(BankAccount):
    """
    A class representing a savings account.

    Attributes:
        balance (float): The current balance of the savings account.
        interest_rate (float): The interest rate for the savings account.

    Methods:
        __init__(overdraft_limit=100): Initializes a new instance of the CheckingAccount class.
        deposit(amount): Deposits the specified amount into the account.
        withdraw(amount): Withdraws the specified amount from the account.
        get_balance(): Returns the current balance of the account.
    """
    # TODO: Define the constructor with a balance and overdraft_limit parameter.
    def __init__(self, balance=0.0, interest_rate=0.0):
        """
        Initializes a new instance of the SavingsAccount class.
        Args:
            balance (float): The initial balance of the account. Defaults to 0.0.
            interest_rate (float): The interest rate for the savings account. Defaults to 0.0.
        """
        self.interest_rate = interest_rate
        super().__init__(balance)

    # TODO: Implement the deposit method with an amount parameter.
    def deposit(self, amount):
        """
        Deposits the specified amount into the savings account.
        Args:
            amount (float): The amount to be deposited.
        """
        # TODO: Add the amount to the balance attribute.
        self.balance += amount

    # TODO: Implement the withdraw method with an amount parameter.
    def withdraw(self, amount):
        """
        Withdraws the specified amount from the savings account.
        Args:
            amount (float): The amount to be withdrawn.
        Raises:
            ValueError: If the specified amount is greater than the current balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        # TODO: Check if the amount is less than or equal to the sum of the balance and overdraft limit.
        # TODO: If the condition is met, subtract the amount from the balance attribute.
        else:
            self.balance -= amount

    def get_balance(self):
        """Returns the current balance of the savings account."""
        return self.balance
