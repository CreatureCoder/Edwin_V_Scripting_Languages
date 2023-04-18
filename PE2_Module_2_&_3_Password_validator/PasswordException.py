#!/usr/bin/env python3

"""
Password Exception

Stores and formats errors.

When one of the conditions above is not met, the code will store the unmet conditions into a dictionary.  The list is
stored and recorded in a log file as: ABC123abc!|symbol|2|1.
"""

import csv

# authorship information
__author__ = 'Edwin Vahlkamp'
__version__ = '1.0'
__date__ = '2023.04.06'
__status__ = 'Development'


class PasswordException(Exception):
    """

    """
    def __init__(self, password, error_type, min_required, char_count):
        """
        Sets up the error in a dictionary and stores the error into a txt file as: ABC123abc!|symbol|2|1.

        :param password:  Stores the password that does not meet a certain condition
        :param error_type:  Stores the type of error the password did not meet
        :param min_required:  Stores the minimum number of the error type the password needs to be valid
        :param char_count:  Stores the number that the password has of the condition that was not met
        """

        self.log = {'password': password,
                    'error_type': error_type,
                    'min_required': min_required,
                    'char_count': char_count}

        with open('password_log.txt', 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([password, error_type, min_required, char_count])
