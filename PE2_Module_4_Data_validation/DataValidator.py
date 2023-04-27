#!/usr/bin/env python3

"""
password_validator
"""

import csv
import re

# Authorship information
__author__ = "Edwin Vahlkamp"
__version__ = "1.0"
__date__ = "2023.04.25"
__status__ = "development"


errors = []


def reading_files():
    global errors

    with open('testing_log.txt', mode='r') as testing, \
         open('invalid_log.txt', mode='r') as invalid, \
         open('valid_log.txt', mode='r') as valid:
        valid_writer = csv.writer(valid, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        invalid_writer = csv.writer(invalid, delimiter='|', quoting=csv.QUOTE_MINIMAL)

        csvWriter = csv.reader(testing, delimiter='|')

        for lines in csvWriter:
            print(lines)
            if len(lines) != 6:
                errors = "C"


def valid_data():
    global errors
    print("valid_data")


def valid_id(id):
    global errors
    if id.isdigit:
        print("Valid id")
    else:
        print("Invalid id")
        errors += "I"


def valid_name(name):
    global errors
    if name.find(',') and name.isalpha:
        print("Found comma")
    else:
        errors += ""


def valid_email(email):
    global errors
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex,email):
        print("The given mail is valid")
    else:
        print("The given mail is invalid")
        errors += "E"


def valid_phone(phone):
    global errors
    rule = re.compile(r'\d{3}-\d{3}-\d{4}')

    if rule.match(phone):
        print("The given phone number is valid")
    else:
        print("The given phone number is invalid")
        errors += "P"


def valid_date(date):
    if date.isdigit:
        return True


def valid_time(time):
    if time.isdigit:
        return True


if __name__ == '__main__':
    reading_files()
    valid_phone('111-222-3333')
