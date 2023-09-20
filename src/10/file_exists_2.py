#!/usr/bin/env python3

if __name__ == '__main__':

    file_name = input('Enter the name of the file we seek: ')

    try:
        open(file_name)
        print('The file exists!')
    except FileNotFoundError:
        print('The file does not exist!')
