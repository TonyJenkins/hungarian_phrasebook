#!/usr/bin/env python3

from math import sqrt


def read_side():
    while True:
        side = int(input('Enter a length: '))

        if side > 0:
            break
        else:
            print('Value out of range. Try again.')

    return side


if __name__ == '__main__':

    side_a = read_side()
    side_b = read_side()

    side_c = sqrt((side_a * side_a) + (side_b * side_b))

    print('Side C length:', side_c)
