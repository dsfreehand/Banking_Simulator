"""This function handles the transfer process for the user."""

# TODO: Pass in the checking_account and savings_account objects.
def handle_transfer(checking, savings):
    """
    Handles the transfer of funds between checking and savings accounts.

    Parameters:
    - checking (Account): The checking account object.
    - savings (Account): The savings account object.

    The function prompts the user to select an account to make a transfer.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After the transfer the function prints the updated balances of both accounts.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to transfer from?")
    # TODO: Prompt the user to select an account to transfer from.
    print("1. Checking Account")
    print("2. Savings Account")
    print("q. Quit")
    # Prompt the user to select an account to transfer from.
    account_choice = input("Enter your choice: ")
    # If the user chooses to quit, return from the function.
    if account_choice == 'q':
        return

    valid_choices = ['1', '2']

    try:
        # TODO: If the selection is in a list of valid choices, i.e ['1', '2']
        if account_choice in valid_choices:
            try:
                # TODO: Prompt the user to enter the amount to transfer and convert it to a float.
                amount = float(input("Enter the amount to transfer: "))
            except ValueError:
                # TODO: Print an error message if the user enters an invalid amount.
                print("Invalid amount entered. Please enter a valid number.")
                # TODO: Call the handle_transfer function recursively if the user enters an invalid amount.
                handle_transfer(checking, savings)
                return

            # TODO: Add an if/else conditional statement to check the account choice,
            if account_choice == '1':
                # TODO: Call the withdraw and deposit methods on the appropriate account.
                checking.withdraw(amount)
                savings.deposit(amount)
            elif account_choice == '2':
                # TODO: Call the withdraw and deposit methods on the appropriate account.
                savings.withdraw(amount)
                checking.deposit(amount)
            # After the transfer call the balances function with the accounts.
            balances(checking, savings)
        else:
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid choice. Please select a valid account.")
    except ValueError as ve:
        print(ve)
        handle_transfer(checking, savings)

def balances(checking, savings):
    """This function prints the account balances for the user."""
    print("\nHere are your account balances:")
    print(f"Checking: ${checking.get_balance():,.2f}")
    print(f"Savings: ${savings.get_balance():,.2f}")
