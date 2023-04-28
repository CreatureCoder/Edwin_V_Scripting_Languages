#!/usr/bin/env python3

"""
password_validator
"""

import csv
import re
from datetime import datetime

# Authorship information
__author__ = "Edwin Vahlkamp"
__version__ = "1.0"
__date__ = "2023.04.25"
__status__ = "development"


errors = ""


def data_validation():
    global errors

    with open('testing_log.txt', mode='r') as testing, \
         open('invalid_log.txt', 'a', newline='\n') as invalid, \
         open('valid_log.txt', 'a', newline='\n') as valid:
        valid_writer = csv.writer(valid, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        invalid_writer = csv.writer(invalid, delimiter='|', quoting=csv.QUOTE_MINIMAL)

        csvWriter = csv.reader(testing, delimiter='|')

        for lines in csvWriter:
            print(lines)
            if len(lines) != 6:
                errors = "C"
                invalid_writer.writerow([errors] + lines)
            else:
                valid_id(lines[0])
                valid_name(lines[1])
                valid_email(lines[2])
                valid_phone(lines[3])
                valid_date(lines[4])
                valid_time(lines[5])

                if len(errors) == 0:
                    valid_writer.writerow(lines)
                else:
                    invalid_writer.writerow([errors] + lines)
                print(errors)


def valid_id(id):
    global errors
    regex = re.compile(r'^[0-9]+$')

    if re.fullmatch(regex, id):
        print("Valid id")
    else:
        print("Invalid id")
        errors = errors + "I"


def valid_name(name):
    global errors
    if name.find(',') and name.isalpha:
        print("Found comma")
    else:
        errors += "N"


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
    global errors
    date_format = "%m/%d/%Y"

    try:
        res = bool(datetime.strptime(date, date_format))
    except ValueError:
        res = False

    if res:
        print("The given date is valid")
    else:
        print("The given date is invalid")
        errors += "D"


def valid_time(time):
    global errors
    regex = re.compile(r'([01]?[0-9]|2[0-3]):[0-5][0-9]')
    if regex.match(time):
        print("The given time is valid")
    else:
        print("The given time is invalid")
        errors += "T"


if __name__ == '__main__':
    data_validation()
