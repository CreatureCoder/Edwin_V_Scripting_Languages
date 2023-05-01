#!/usr/bin/env python3

"""
data_validator

Assesses data from a file, validate if the data, and then sends the data to different files depending if the data is
good or not.

Uses a testing_log.txt for the data and a valid_log.txt and an invalid_log.txt to store the data.

Each string of data must consist of 6 parts in the correct formate:
    id|last name,first name|email|phone number|date|time

Example of valid data:
    1|Johnson,Debbie|dejohns2@wsc.edu|111-222-3333|12/31/2019|13:40

There are seven different errors the may occur:
C = invalid data element count
I = invalid id
N = invalid name
E = invalid email
P = invalid phone number
D = invalid date
T = invalid time

Note: if C was the error, there will not be any other errors.

If any of the following errors occur the string will be written to the invalid_log.txt with the type or types of errors
at the beginning of the string.

Example of written invalid data:
    IPDT|abc|Johnson|dejohns2@gmail.com|1112223333|12/31/80|1340

If no errors occur then the valid data will be written to the valid_log.txt with some formatting.  The first name will
be first and last name last, the phone number dashes becomes periods, and the data will be year-month-day.

Example of written valid data:
    1,Debbie,Johnson,dejohns2@wsc.edu,111.222.3333,2019-12-31,13:40

"""

import csv
import re
import datetime

# Authorship information
__author__ = "Edwin Vahlkamp"
__version__ = "1.0"
__date__ = "2023.04.25"
__status__ = "development"

# stores the errors a string might trigger
errors = ""


def data_validation():
    """
    Opens the testing_log.txt, valid_log.txt, and invalid_log.txt and reads and assesses line by line of data.  First
    test if id is valid, then name is valid, email is valid, phone number is valid, date is valid, and see if time is
    valid.

    If there is one of the validation fails, add the corresponding errors to the errors and write the entire line to
    the invalid log with the errors that the data incur.

    If there is nothing in errors, the data is processed and is written to the valid_log

    :return: None
    """
    global errors

    with open('testing_log.txt', mode='r') as testing, \
            open('valid_log.txt', 'a', newline='\n') as valid, \
         open('invalid_log.txt', 'a', newline='\n') as invalid:
        valid_writer = csv.writer(valid, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        invalid_writer = csv.writer(invalid, delimiter='|', quoting=csv.QUOTE_MINIMAL)

        csvWriter = csv.reader(testing, delimiter='|')

        for lines in csvWriter:
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
                    name = lines[1]

                    # Formats the name
                    lines[1] = name[name.find(',')+1:]
                    lines.insert(2, name[:name.find(',')])
                    # Formats the phone number from dashes to periods
                    lines[4] = lines[4].replace('-', '.')
                    # Formats the date form month/day/year to year-month-day
                    date_trans = datetime.datetime.strptime(lines[5], '%m/%d/%Y')
                    lines[5] = date_trans.strftime("%Y-%m-%d")

                    valid_writer.writerow(lines)
                else:
                    invalid_writer.writerow([errors] + lines)
            errors = ""


def valid_id(id):
    """
    If the supposed id matches with the regex formate, do nothing otherwise add an 'I' to the string of errors

    :param id: Gets the first piece in the string of data which is the supposed id
    :return: None
    """
    global errors
    regex = re.compile(r'^[0-9]+$')

    if not re.fullmatch(regex, id):
        errors +="I"


def valid_name(name):
    """
    If the supposed name that has a ',' and matches the regex formate, do nothing otherwise add an 'N' to the string of
    errors

    :param name: Gets the second piece in the string of data which is the supposed name
    :return: None
    """
    global errors
    regex = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$')

    if not name.find(',') and re.fullmatch(regex, name):
        errors += "N"


def valid_email(email):
    """
    If the supposed email matches with the regex formate, do nothing otherwise add an 'E' to the string of errors

    :param email: Gets the third piece in the string of data which is the supposed email
    :return: None
    """
    global errors
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if not re.fullmatch(regex,email):
        errors += "E"


def valid_phone(phone):
    """
    If the supposed phone matches with the regex formate, do nothing otherwise add an 'P' to the string of errors

    :param phone: Gets the fourth piece in the string of data which is the supposed phone number
    :return: None
    """
    global errors
    rule = re.compile(r'\d{3}-\d{3}-\d{4}')

    if not rule.match(phone):
        errors += "P"


def valid_date(date):
    """
    If the supposed date matches with the regex formate, do nothing otherwise add an 'D' to the string of errors

    :param date: Gets the fifth piece in the string of data which is the supposed date at which was entered
    :return: None
    """
    global errors
    date_format = "%m/%d/%Y"

    try:
        res = bool(datetime.datetime.strptime(date, date_format))
    except ValueError:
        res = False

    if not res:
        errors += "D"


def valid_time(time):
    """
    If the supposed time matches with the regex formate, do nothing otherwise add an 'T' to the string of errors

    :param time: Gets the last piece in the string of data which is the supposed time at which was entered
    :return: None
    """
    global errors
    regex = re.compile(r'([01]?[0-9]|2[0-3]):[0-5][0-9]')

    if not regex.match(time):
        errors += "T"


if __name__ == '__main__':
    data_validation()

