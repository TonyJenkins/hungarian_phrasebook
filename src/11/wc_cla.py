#!/usr/bin/env python3


import sys


if __name__ == '__main__':
    file_name = sys.argv[1]

    f = open(file_name, 'r')
    lines = len(f.readlines())

    print(f'Line Count: {lines}.')
