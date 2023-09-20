#!/usr/bin/env python3

from math import sqrt

if __name__ == '__main__':

    side_a = int(input('Enter the length of side A: '))
    side_b = int(input('Enter the length of side B: '))

    side_c = sqrt((side_a * side_a) + (side_b * side_b))

    print('Side C length:', side_c)
