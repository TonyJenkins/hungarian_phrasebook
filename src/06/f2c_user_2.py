#!/usr/bin/env python3

if __name__ == '__main__':

    start_f = int(input('Enter the starting value: '))
    end_f = int(input('Enter the ending value: '))
    increment = int(input('Enter the increment '))

    for fahrenheit in range(start_f, end_f, increment):
        celsius = (fahrenheit - 32) * 5 / 9
        print('Fahrenheit ', fahrenheit,  'F Celsius Equivalent is ', celsius, 'C', sep='')
