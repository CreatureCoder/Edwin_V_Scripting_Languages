#!/usr/bin/env python3

"""
Students adds the modifier to the main menuu
"""

import data_validation as dv


def list_students(students):
    if students == {}:
        print("  There are no students to list")
        return

    print(f'{"=" * 4:>4} {"=" * 15:>15} {"=" * 15:>15}')
    print(f'{"ID":>4} {"First Name":<15} {"Last Name":<15}')
    print(f'{"=" * 4:>4} {"=" * 15:>15} {"=" * 15:>15}')
    for student_id, student_name in students.items():
        first_name, last_name = student_name.values()
        print(f'{student_id:>4} {first_name:<15} {last_name:<15}')


def add_student(students, next_student_id):
    print("Add Students")           # remember to remove this later
    first_name = dv.get_string("Please enter the student's first Name")
    last_name = dv.get_string("Please enter the student's last Name")

    students[next_student_id] = {'first_name': first_name, 'last_name': last_name}


def update_student(students):
    if students == {}:
        print("  There are no students to update")
        return

    print("Update Students")        # remember to remove this later
    student_id = dv.get_positive_num("Please enter the ID that is to be updated")
    if student_id > len(students):
        print(f'   Student ID{student_id} was not found.')
        return

    student = students[student_id]
    first_name, last_name = student.values()

    first_update_name = dv.get_string("please enter the student's update first name")
    last_update_name = dv.get_string("Please enter the student's update last name")

    yes_or_no = dv.get_yes_no(f'Please confirm updating {first_name} {last_name} to {first_update_name} '
                              f'{last_update_name}')
    if yes_or_no == False:
        return

    students[student_id] = {'first_name': first_update_name, 'last_name': last_update_name}


def delete_student(students):
    print("Delete Students")


if __name__ == '__main__':
    help('student_maintenance')