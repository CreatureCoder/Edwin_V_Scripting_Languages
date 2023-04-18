#!/usr/bin/env python3

"""
Password Testing

Pre-created testing grounds for passwords.

Pre-creates how to display the error or errors a password invokes.

Uses default and the advance PasswordValidator.

GitHub URL: https://github.com/CreatureCoder/Edwin_V_Scripting_Languages.git
"""

import PasswordValidator as PV
import AdvancePasswordValidator as APV

# authorship information
__author__ = 'Edwin Vahlkamp'
__version__ = '1.0'
__date__ = '2023.04.06'
__status__ = 'Development'


def display_errors(errors):
    """
    Displays the errors a password does not meet and displays it or them as: ABC123abc! password must contain 2 symbol
    but yours only contained 1.

    :param errors:  Stores the list of errors a password does not meet
    :return:  none
    """
    print("Invalid Password")
    for e in errors:
        print(f"{e.log['password']} password must contain {e.log['min_required']} {e.log['error_type']} "
              f"but yours only contained {e.log['char_count']}")


def default_validation():
    """
    Tests different passwords with the PasswordValidator.

    :return:  none
    """

    pv = PV.PasswordValidator(debug_mode=True)
    if pv.is_valid("ABC123abc!"):
        print("Valid Password")
    else:
        display_errors(pv.errors)

    if pv.is_valid("Abb12!*"):
        print("Valid Password")
    else:
        display_errors(pv.errors)

    if pv.is_valid("AAb12!*"):
        print("Valid Password")
    else:
        display_errors(pv.errors)


def advance_validtion():
    """
    Tests different passwords with the AdvancePasswordValidator.

    :return:  none
    """

    apv = APV.AdvancePasswordValidator(debug_mode=True)
    if apv.is_valid("ABC123abc!&"):
        print("Valid Password")
    else:
        display_errors(apv.errors)


if __name__ == '__main__':
    default_validation()
    advance_validtion()
