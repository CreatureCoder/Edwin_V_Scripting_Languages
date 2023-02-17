#!/usr/bin/env python3

"""
Students adds the modifier to the main menu
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
    if students == {}:
        print("  There are no students to update")
        return

    print("Delete Students")
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


if __name__ == '__main__':
    help('student_maintenance')