#!/usr/bin/env python3

"""
Password Validator
"""

import inspect
import csv

__author__ = 'Edwin Vahlkamp'
__version__ = '1.0'
__date__ = '2023.04.06'
__status__ = 'Development'

class PasswordException(Exception):
    def __init__(self, password, error_type, min_required, char_count):
        self.log - {'password': password,
                    'type': error_type,
                    'min_required': min_required,
                    'char_count': char_count}

        with open('password_log.txt', 'a', newlin='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([password, error_type, min_required, char_count])


class PasswordValidator:
    __UPPERCASE_MIN = 2
    __LOWERCASE_MIN = 2
    __DIGIT_MIN = 2
    __SYMBOL_MIN = 2

    def __init__(self, password=None, debug_mode=False):
        self.__password = password
        self.__debug_mode = debug_mode
        self.__errors = []

    def __str__(self):
        if self.__password is None:
            return "None"
        else:
            return self.__password


    def __is_uppercase_valid(self):
        char_count = sum(1 for c in self.__password if c.isupper())  # can stop counting early

        if self.__debug_mode:
            print(f"{char_count:3d} = {inspect.currentframe().f_code.co_name}")

        if char_count >= 2:
            return True

        else:
            print(f"Password must have at least {PasswordValidator.__UPPERCASE_MIN} uppercase letters.")
            return False


    def __is_lowercase_valid(self):
        char_count = sum(1 for c in self.__password if c.islower())  # can stop counting ear

        if self.__debug_mode:
            print(f"{char_count:3d} = {inspect.currentframe().f_code.co_name}")

        if char_count >= 2:
            return True

        else:
            print(f"Password must have at least {PasswordValidator.__LOWERCASE_MIN} lowercase letters.")
            return False


    def is_valid(self, password=None):

        if self.__debug_mode:
            print("+++++++++DEBUG MODE+++++++++")

        if password is None:
            raise Exception("password can not be empty")

        self.__password = password
        uppercase_valid = self.__is_uppercase_valid()
        lowercase_valid = self.__is_lowercase_valid()

        if uppercase_valid and lowercase_valid:
            return True
        else:
            return False


pv = PasswordValidator(debug_mode=True)
print(pv.is_valid("ABC123abc!"))
