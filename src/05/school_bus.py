#!/usr/bin/env python3

if __name__ == '__main__':

    STUDENTS_PER_BUS = 46

    number_of_students = int(input('How many students are there? '))

    buses_needed = number_of_students // STUDENTS_PER_BUS
    students_left = number_of_students % STUDENTS_PER_BUS

    print('Buses Needed: ', buses_needed)
    print('Students Left:', students_left)
