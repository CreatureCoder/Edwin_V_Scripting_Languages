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


def reading_files():
    with open('testing_log.txt', mode='r', newline='\n') as testing:

        csvFile = csv.reader(testing)

        for lines in csvFile:
            yield(lines)


def valid_data():

    for line in reading_files():
        data = line
        print(data[:1])

        print(data)


def valid_id(id):
    if id.isdigit:
        return True


def valid_name(name):
    if name.isalpa:
        return True


def valid_email(email):
    regex = re.compile(r'[A-Za-z0-9]+[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2.})+')


def valid_phone(phone):
    if phone.isdigit:
        return True


def valid_date(date):
    if date.isdigit:
        return True


def valid_time(time):
    if time.isdigit:
        return True


if __name__ == '__main__':
    valid_data()
