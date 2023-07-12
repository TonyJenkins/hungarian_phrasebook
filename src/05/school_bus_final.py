#!/usr/bin/env python3

if __name__ == '__main__':

    try:
        students_per_bus = int(input('What is the bus size? '))
        number_of_students = int(input('How many students are there? '))

        buses_needed = number_of_students // students_per_bus
        students_left = number_of_students % students_per_bus

        print('Buses Needed: ', buses_needed)
        print('Students Left:', students_left)

    except ValueError:
        print('Please enter an integer.')
    except ZeroDivisionError:
        print('Bus size cannot be zero.')
