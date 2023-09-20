#!/usr/bin/env python3

if __name__ == '__main__':

    file_name = input('Enter the name of the file: ')

    try:
        f = open(file_name)
        lines = len(f.readlines())

        f.close()

        print('Lines in the file:', lines)

    except FileNotFoundError:
        print('Error: File cannot be found.')
