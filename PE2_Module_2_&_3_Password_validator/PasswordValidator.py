#!/usr/bin/env python3

"""
Password Validator

Allows end users to validate basic password.

Passwords must consist of a minimum of two capital letters, two lowercase letters, two digits, and two symbols.

When one of the conditions above is not met, the code will call the PasswordException file and store the errors in a
list.  The list is used for storing the different unmet conditions a password does not meet.

End users can choose the pre-created testing grounds or create their own password testing grounds to display if the
password is not valid and how they want to display the errors.

End users will call is_valid function to test if a password is valid or not.

End users can deside to activate the DEGUG MODE to see the number of uppercase letters, lowercase letters, digits, and
symbols the password contains.

GitHub URL: https://github.com/CreatureCoder/Edwin_V_Scripting_Languages.git
"""

import inspect
import PasswordException as PE

# authorship information
__author__ = 'Edwin Vahlkamp'
__version__ = '1.0'
__date__ = '2023.04.06'
__status__ = 'Development'


class PasswordValidator:
    """
    Class that pre-sets the limits of the minimal number of uppercase letters, lowercase letters, digits, and symbols.

    Stores the code to validate all mentioned above and tells if all the following conditions are met
    """
    UPPERCASE_MIN = 2
    LOWERCASE_MIN = 2
    DIGIT_MIN = 2
    SYMBOL_MIN = 2

    def __init__(self, debug_mode=False):
        """
        Sets the defaults of the password, debug_mode, and set up the errors list.
        :param debug_mode:  Allows end user to turn the debug mode on or off
        """
        self.password = "unknown"
        self.debug_mode = debug_mode
        self.errors = []

    def __str__(self):
        """
        Overriding the default that display the object type and memory reference to instead display the password.
        :return:  the password
        """
        return self.password

    def __validate_uppercase(self):
        """
        Validates if the password has at least two capital letters.

        If not met, calls PasswordException, stores the error, and adds the error to errors list.
        :return:  none
        """
        char_count = sum(1 for c in self.password if c.isupper())  # can stop counting early

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.UPPERCASE_MIN:
            raise PE.PasswordException(self.password, 'uppercase', PasswordValidator.UPPERCASE_MIN, char_count)

    def __validate_lowercase(self):
        """
        Validates if the password has at least two lowercase letters.

        If not met, calls PasswordException, stores the error, and adds the error to errors list.
        :return:  none
        """
        char_count = sum(1 for c in self.password if c.islower())  # can stop counting ear

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.LOWERCASE_MIN:
            raise PE.PasswordException(self.password, 'lowercase', PasswordValidator.LOWERCASE_MIN, char_count)

    def __validate_digit(self):
        """
        Validates if the password has at least two digit.

        If not met, calls PasswordException, stores the error, and adds the error to errors list.
        :return:  none
        """
        char_count = sum(1 for c in self.password if c.isdigit())  # can stop counting ear

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.DIGIT_MIN:
            raise PE.PasswordException(self.password, 'digit', PasswordValidator.DIGIT_MIN, char_count)

    def __validate_symbol(self):
        """
        Validates if the password has at least two symbols.

        If not met, calls PasswordException, stores the error, and adds the error to list.
        :return:  none
        """
        char_count = sum(1 for c in self.password if not c.isdigit() and not c.isalpha())  # can stop counting ear

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.SYMBOL_MIN:
            raise PE.PasswordException(self.password, 'symbol', PasswordValidator.SYMBOL_MIN, char_count)

    def is_valid(self, password):
        """
        Determines if the following conditions are met

        If any of the conditions are not met, calls PasswordException, stores the error, and adds the error to errors
        list.
        :param password:  stores the password the end user enters
        :return:  True if all conditions are met.  False if one or more are not met
        """
        self.password = password

        self.errors.clear()

        if self.debug_mode:
            print("+++++++++DEBUG MODE+++++++++")
            print("password =", self)

        try:
            self.__validate_uppercase()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_lowercase()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_digit()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_symbol()
        except PE.PasswordException as e:
            self.errors.append(e)

        if len(self.errors) == 0:
            return True
        else:
            return False
