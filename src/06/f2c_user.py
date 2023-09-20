#!/usr/bin/env python3

if __name__ == '__main__':

    fahrenheit = float(input("Enter the Fahrenheit Temperature: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print('Celsius Equivalent is ', celsius, 'C', sep='')
