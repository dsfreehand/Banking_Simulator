def balances(checking, savings):
    """
    Displays the current balances of the checking and savings accounts.

    Args:
        checking (CheckingAccount): The user's checking account.
        savings (SavingsAccount): The user's savings account.
    """
    print(f"Checking Account Balance: ${checking.get_balance():,.2f}")
    print(f"Savings Account Balance: ${savings.get_balance():,.2f}")
