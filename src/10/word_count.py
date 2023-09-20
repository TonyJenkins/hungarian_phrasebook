#!/usr/bin/env python3

if __name__ == '__main__':

    file_name = input('Enter the name of the file: ')

    f = open(file_name)
    lines = len(f.readlines())

    print('Lines in the file:', lines)
