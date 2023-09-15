#!/usr/bin/env python3

if __name__ == '__main__':

    file_name = input('Enter the name of the file: ')

    try:
        f = open(file_name)

        lines = f.readlines()

        f.close()

        characters = 0
        for line in lines:
            characters += len(line) - 1

        print('Lines in the file:     ', len(lines))
        print('Characters in the file:', characters)

    except FileNotFoundError:
        print('Error: File cannot be found.')
