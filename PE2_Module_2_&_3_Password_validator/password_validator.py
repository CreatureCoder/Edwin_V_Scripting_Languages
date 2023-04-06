#!/usr/bin/env python3

"""
Password Validator
"""

import inspect

__author__ = 'Edwin Vahlkamp'
__version__ = '1.0'
__date__ = '2023.04.06'
__status__ = 'Development'

class PasswordValidator:
    __UPPERCASE_MIN = 2
    __LOWERCASE_MIN = 2
    __DIGIT_MIN = 2
    __SYMBOL_MIN = 2

    def __init__(self, password=None, debug_mode=False):
        self.__password = password
        self.__debug_mode = debug_mode

    def __str__(self):
        if self.__password is None:
            return "None"
        else:
            return self.__password


    def __is_uppercase_valid(self):
        count = sum(1 for c in self.__password if c.isupper())  # can stop counting early

        if self.__debug_mode:
            print(f"{count:3d} = {inspect.currentframe().f_code.co_name}")

        if count >= 2:
            return True

        else:
            print(f"Password must have at least {PasswordValidator.__UPPERCASE_MIN} uppercase letters.")
            return False

    def is_valid(self, password=None):

        if self.__debug_mode:
            print("+++++++++DEBUG MODE+++++++++")

        if password is None:
            raise Exception("password can not be empty")

        self.__password = password
        uppercase_valid = self.__is_uppercase_valid()

        if uppercase_valid:
            return True
        else:
            return False


pv = PasswordValidator(debug_mode=True)
print(pv.is_valid("ABC123abc!"))
