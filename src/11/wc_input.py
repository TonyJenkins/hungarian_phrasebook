#!/usr/bin/env python3

if __name__ == '__main__':
    file_name = input('Enter the file name: ')

    f = open(file_name, 'r')
    lines = len(f.readlines())

    print(f'Line Count: {lines}.')
