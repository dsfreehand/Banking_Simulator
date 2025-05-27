"""This function handles the deposit process for the user."""

# TODO: Build out the handle_deposit function
# TODO: Pass in the checking account and savings account objects.
def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    # TODO: Prompt the user to select an account and make a deposit.
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
                    # TODO: Prompt the user to enter the amount to deposit and convert it to a float.
                    amount = float(input("Enter the amount to deposit into Checking Account: "))
                # Use the ValueError as an exception.
                except ValueError:
                    # TODO: Print an error message if the user enters an invalid amount.
                    print("Invalid amount entered. Please enter a valid number.")

                    # TODO: Call the handle_deposit function recursively for an invalid amount.
                    handle_deposit(checking, savings)

                    # TODO: Ensure the function returns after the recursive call.
                    return

                # TODO: Call the deposit method on the appropriate account.
                checking.deposit(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                print(f"Deposited ${amount:.2f} into Checking Account.")
                # TODO: Format the balance to two decimal places and thousands.
                print(f"New Checking Account Balance: ${checking.get_balance():,.2f}")
            else:
                try:
                    # TODO: Prompt the user to enter the amount to deposit and convert it to a float.
                    amount = float(input("Enter the amount to deposit into Savings Account: "))
                except ValueError:
                    print("Invalid amount entered. Please enter a valid number.")
                    handle_deposit(checking, savings)
                    return

                # TODO: Call the deposit method on the appropriate account.
                savings.deposit(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                print(f"Deposited ${amount:.2f} into Savings Account.")
                # TODO: Format the balance to two decimal places and thousands.
                print(f"New Savings Account Balance: ${savings.get_balance():,.2f}")
        else:
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid choice. Please select a valid account.")

    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)
