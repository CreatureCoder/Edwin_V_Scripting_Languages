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

    def __init__(self, debug_mode=False):
        self.__password = "unknown"
        self.__debug_mode = debug_mode
        self.__errors = []

    def __str__(self):
        return self.__password

    def __validate_uppercase(self):
        char_count = sum(1 for c in self.__password if c.isupper())  # can stop counting early

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.__UPPERCASE_MIN:
            raise PasswordException(self.__password, 'uppercase', PasswordValidator.__UPPERCASE_MIN, char_count)

    def __validate_lowercase(self):
        char_count = sum(1 for c in self.__password if c.islower())  # can stop counting ear

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.__LOWERCASE_MIN:
            raise PasswordException(self.__password, 'lowercase', PasswordValidator.__LOWERCASE_MIN, char_count)

    def __validate_digit(self):
        char_count = sum(1 for c in self.__password if c.isdigit())  # can stop counting ear

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.__DIGIT_MIN:
            raise PasswordException(self.__password, 'digit', PasswordValidator.__DIGIT_MIN, char_count)

    def __validate_symbol(self):
        char_count = sum(1 for c in self.__password if not c.isdigit() and c.isalpha)  # can stop counting ear

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.__SYMBOL_MIN:
            raise PasswordException(self.__password, 'symbol', PasswordValidator.__SYMBOL_MIN, char_count)

    def is_valid(self, password):
        self.__password = password

        if self.__debug_mode:
            print("+++++++++DEBUG MODE+++++++++")
            print("password =", self)

        try:
            self.__validate_uppercase()
        except PasswordException as e:
            self.__errors.append(e)

        try:
            self.__validate_lowercase()
        except PasswordException as e:
            self.__errors.append(e)

        try:
            self.__validate_digit()
        except PasswordException as e:
            self.__errors.append(e)

        try:
            self.__validate_symbol()
        except PasswordException as e:
            self.__errors.append(e)

        if len(self.__errors) == 0:
            return True
        else:
            for e in self.__errors:
                print(f"password must contain {e.log['min_required']} {e.log['error_type']} "
                      f"but yours only contained {e.log['char_count']}")
                return False


pv = PasswordValidator(debug_mode=True)
if pv.is_valid("ABC123abc!"):
    print("Valid Password")
else:
    print("Invalid Password")

if pv.is_valid("Abb12!*"):
    print("Valid Password")
else:
    print("Invalid Password")

if pv.is_valid("AAb12!*"):
    print("Valid Password")
else:
    print("Invalid Password")
