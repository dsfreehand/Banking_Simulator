""" This class validates the email addresses and password when logging on."""

class Validation:
    """ This class contains methods for validating email addresses and passwords."""
    @staticmethod
    # TODO: Implement the validate_email method using the staticmethod decorator.
    # TODO: The method should take an email parameter and return True if the email contains an "@" symbol.

    @staticmethod
    # TODO: Implement the validate_password method using the staticmethod decorator.
    def validate_email(email):
        """Validates the email address."""
        # TODO: Implement the password length validation logic.
        return "@" in email

    @staticmethod
    def validate_password(password):
        """Validates the password."""
        # TODO: Check if the password is at least 8 characters long if not return False.
        if len(password) < 8:
            return False

        # TODO: Set the initial values for uppercase, lowercase, digit, and special characters to False.
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_characters = "!@#$%^&*"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_characters:
                has_special = True

        # Return the boolean value based on the conditions.
        return has_upper and has_lower and has_digit and has_special
