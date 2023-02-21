#!/usr/bin/env python3

"""
Students maintenance that contains functions that list the students in the system, add students to the system, update
the students in the system, and delete any students in the system

Author: Edwin Vahlkamp
Date: February 20, 2023
GitHub repository URL: https://github.com/CreatureCoder/Edwin_V_Scripting_Languages.git
"""

import data_validation as dv


def list_students(students):
    """
    Displays all the students that are currently in the system.  If there are no students in the system, then displays
    "There are no students to list" and return back to the menu
    :param students: gets the list of students in the system
    :return: gets out of the system if there are no students in the system
    """

    if students == {}:
        print("  There are no students to list")
        return

    print(f'{"=" * 4:>4} {"=" * 15:>15} {"=" * 15:>15}')
    print(f'{"ID":>4} {"First Name":<15} {"Last Name":<15}')
    print(f'{"-" * 4:>4} {"-" * 15:>15} {"-" * 15:>15}')
    for student_id, student_name in students.items():
        first_name, last_name = student_name.values()
        print(f'{student_id:>4} {first_name:<15} {last_name:<15}')
    print(f'{"=" * 4:>4} {"=" * 15:>15} {"=" * 15:>15}')


def add_student(students, next_student_id):
    """
    Prompts the user to input the student's first and last name that is to be added to the system.  If the user inputs
    an invalid input, the system will loop until a valid input has been entered
    :param students: gets the current list of students in the system
    :param next_student_id: gets the next id to be added to the system
    :return: returns the list with an added student
    """

    print("Add Student")
    print("-----------")
    first_name = dv.get_string("Please enter the student's first Name")
    last_name = dv.get_string("Please enter the student's last Name")

    students[next_student_id] = {'first_name': first_name, 'last_name': last_name}

    print(f'\nStudent ID #{next_student_id}: {first_name} {last_name} has been added')


def update_student(students):
    """
    Prompts the user to input a valid student id and asks if the user want to change the first name, last name or both.
    Users can enter a blank line to keep the name in question.  Program prompts the user of if the user wants to change
    the name with a yes or no prompt.  If no, returns to main menu.  If the id is out of the range, it will send the
    user back to the menu.
    :param students: gets the current list of students in the system
    :return: If set of parameters are meet, returns nothing otherwise the system will update the name the user wants to
             change on the list
    """

    if students == {}:
        print("  There are no students to update")
        return

    print("Update Student")
    print("--------------")
    student_id = dv.get_positive_num("Please enter the ID that is to be updated")
    if student_id > len(students):
        print(f'   Student ID{student_id} was not found.')
        return

    student = students[student_id]
    first_name, last_name = student.values()

    print(f'The student chosen to be updated is {first_name} {last_name}\n')

    first_update_name = input("Please enter the student's update first name or press enter to keep "
                              + first_name + ": ")
    last_update_name = input("Please enter the student's update last name or press enter to keep "
                             + last_name + ": ")

    if first_update_name == '' and last_update_name == '' or \
       first_update_name == first_name and last_update_name == last_name:
        print("\nNo data changed.  Update Cancelled\n")
        return

    elif first_update_name == '':
        yes_or_no = dv.get_yes_no(f'\nPlease confirm updating {first_name} {last_name} to {first_name} '
                                  f'{last_update_name}')
        if yes_or_no == False:
            print("No data changed.  Update Cancelled")
            return

        students[student_id] = {'first_name': first_name, 'last_name': last_update_name}

    elif last_update_name == '':
        yes_or_no = dv.get_yes_no(f'\nPlease confirm updating {first_name} {last_name} to {first_update_name} '
                                  f'{last_name}')
        if yes_or_no == False:
            print("No data changed.  Update Cancelled")
            return

        students[student_id] = {'first_name': first_update_name, 'last_name': last_name}

    else:
        yes_or_no = dv.get_yes_no(f'\nPlease confirm updating {first_name} {last_name} to {first_update_name} '
                                  f'{last_update_name}')
        if yes_or_no == False:
            print("No data changed.  Update Cancelled")
            return

        students[student_id] = {'first_name': first_update_name, 'last_name': last_update_name}

    print("Update confirm\n")


def delete_student(students):
    """
    Prompts the user to input a student id that the user wants to delete.  Program prompts the user of if the user wants
    to change the name with a yes or no prompt.  If no, the program will send user to the main menu.  If the id is out
    of the range, it will send the user back to the menu.
    :param students: gets the current list of students in the system
    :return: If the user did not want to delete returns nothing, otherwise returns a list with the deleted person the
             user wanted to delete
    """

    if students == {}:
        print("  There are no students to update")
        return

    print("Delete Student")
    print("--------------")
    student_id = dv.get_positive_num("Please enter the ID that is to be updated")
    if student_id > len(students):
        print(f'   Student ID{student_id} was not found.')
        return

    student = students[student_id]
    first_name, last_name = student.values()

    yes_or_no = dv.get_yes_no(f'Please confirm to delete {first_name} {last_name} ')
    if yes_or_no == False:
        print("No data changed.  Delete Cancelled")
        return

    del students[student_id]
    print("Student Deleted")


if __name__ == '__main__':
    help('student_maintenance')