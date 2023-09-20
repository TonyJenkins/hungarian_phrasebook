#!/usr/bin/env python3


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':

    for count in range(-10, 11):
        if is_even(count):
            print(count)
