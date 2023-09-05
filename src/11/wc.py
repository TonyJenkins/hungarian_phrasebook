#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    try:
        file_name = sys.argv[1]

        f = open(file_name, 'r')
        lines = len(f.readlines())

        print(f'Line Count: {lines}.')

    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument.')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')
