#!/usr/bin/env python3

"""
Advance Password Validator

Allows end users to validator passwords with more conditions.

Passwords must consist of a minimum of two capital letters, two lowercase letters, two digits, and two specific symbols,
and requires a minimum length of eight and a maximum length of 30.  The valid symbols are:!, @, #, $, and *.

When one of the conditions above is not met, the code will call the PasswordException file and store the errors in a
list.  The list is used for storing the different unmet conditions a password does not meet.

End users can choose the pre-created testing grounds or create their own password testing grounds to display if the
password is not valid and how they want to display the errors.

End users will call is_valid function to test if a password is valid or not.

End users can deside to activate the DEGUG MODE to see the number of uppercase letters, lowercase letters, digits, valid
symbols, and the number af characters the password contains.
"""


import inspect
import PasswordValidator as PV
import PasswordException as PE

# authorship information
__author__ = 'Edwin Vahlkamp'
__version__ = '1.0'
__date__ = '2023.04.06'
__status__ = 'Development'


class AdvancePasswordValidator(PV.PasswordValidator):
    """
    Subclass of PasswordValidator

    Class that pre-sets the limits of the minimal number of valid symbols, maximum length and minimum length.

    Stores the code to validate all mentioned above and tells if all the following conditions are met
    """

    VALID_SYMBOLS = ('!', '@', '#', '$', '*')
    MIN_LIMIT = 8
    MAX_LIMIT = 30

    # min requirement
    # max limit
    # specific symbols

    def __init__(self, debug_mode=False):
        super().__init__(debug_mode)

    def __validate_symbols(self):
        """
        Validates if the password has at least two valid symbols.

        The valid symbols are stored in VALID_SYMBOLS.

        If not met, calls PasswordException, stores the error, and adds the error to errors list.
        :return:  none
        """
        char_count = sum(1 for c in self.password if c in AdvancePasswordValidator.VALID_SYMBOLS)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < super().SYMBOL_MIN:
            raise PE.PasswordException(self.password, 'valid symbols', super().SYMBOL_MIN, char_count)

    def __validate_min(self):
        """
        Validates if the password has at least eight characters.

        If not met, calls PasswordException, stores the error, and adds the error to errors list.
        :return:  none
        """
        char_count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < AdvancePasswordValidator.MIN_LIMIT:
            raise PE.PasswordException(self.password, 'min limit', AdvancePasswordValidator.MIN_LIMIT, char_count)

    def __validate_max(self):
        """
        Validates if the password has at most 30 characters.

        If not met, calls PasswordException, stores the error, and adds the error to errors list.
        :return:  none
        """
        char_count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count > AdvancePasswordValidator.MAX_LIMIT:
            raise PE.PasswordException(self.password, 'max limit', AdvancePasswordValidator.MAX_LIMIT, char_count)

    def is_valid(self, password):
        """
        If the following conditions from the super class is met, then determines if the following advance conditions
        are met.

        If any of the conditions are not met, calls PasswordException, stores the error, and adds the error to errors
        list.
        :param password:  Stores the password
        :return:  none
        """
        if super().is_valid(password):

            try:
                self.__validate_symbols()
            except PE.PasswordException as e:
                self.errors.append(e)

            try:
                self.__validate_min()
            except PE.PasswordException as e:
                self.errors.append(e)

            try:
                self.__validate_max()
            except PE.PasswordException as e:
                self.errors.append(e)

            if len(self.errors) == 0:
                return True
            else:
                return False
