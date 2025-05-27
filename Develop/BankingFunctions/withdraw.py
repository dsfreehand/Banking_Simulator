"""This function handles the withdrawal process for the user."""

# TODO: Pass in the checking_account and savings_account objects.
def handle_withdrawal(checking, savings):
    """
    Handles the withdrawal of funds for checking and savings accounts.

    Parameters:
    - checking (CheckingAccount): The checking account object.
    - savings (SavingsAccount): The savings account object.

    The function prompts the user to select an account and make a withdrawal.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After each withdrawal, the function prints the updated balance of the respective account.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to make a withdrawal?")
    # TODO: Prompt the user to select an account to make a withdrawal.
    print("1. Checking Account")
    print("2. Savings Account")
    print("q. Quit")
    # TODO: If the user chooses to quit, return from the function.


    try:
        # TODO: If the selection is in a list of valid choices, i.e ['1', '2']
        account_choice = input("Enter your choice (1-2 or 'q' to quit): ").strip().lower()
        if account_choice == 'q':
            return
        valid_choices = ['1', '2']
        if account_choice in valid_choices:
            if account_choice == '1':
                try:
                    # TODO: Prompt the user to enter the amount to withdraw and convert it to a float.
                    amount = float(input("Enter the amount to withdraw from Checking Account: "))
                # Use the ValueError as an exception.
                except ValueError:
                    # TODO: Print an error message if the user enters an invalid amount.
                    print("Invalid amount entered. Please enter a valid number.")

                    # TODO: Call the handle_withdrawal function recursively for an invalid amount.
                    handle_withdrawal(checking, savings)

                    # TODO: Ensure the function returns after the recursive call.
                    return

                # TODO: Call the withdraw method on the appropriate account.
                checking.withdraw(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                print(f"Withdrew ${amount:.2f} from Checking Account.")
                # TODO: Format the balance to two decimal places and thousands.
                print(f"New Checking Account Balance: ${checking.get_balance():,.2f}")
            else:
                try:
                    amount = float(input("Enter the amount to withdraw from Savings Account: "))
                except ValueError:
                    print("Invalid amount entered. Please enter a valid number.")
                    handle_withdrawal(checking, savings)
                    return

                # TODO: Call the withdraw method on the appropriate account.
                savings.withdraw(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                print(f"Withdrew ${amount:.2f} from Savings Account.")
                # TODO: Format the balance to two decimal places and thousands.
                print(f"New Savings Account Balance: ${savings.get_balance():,.2f}")
        else:
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid choice. Please select a valid account.")
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    
    except ValueError as e:
        print(e)
        handle_withdrawal(checking, savings)
