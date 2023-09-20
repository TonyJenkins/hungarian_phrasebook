#!/usr/bin/env python3

if __name__ == '__main__':

    for fahrenheit in range(30, 81, 5):
        celsius = (fahrenheit - 32) * 5 / 9
        print('Fahrenheit ', fahrenheit,  'F Celsius Equivalent is ', celsius, 'C', sep='')
