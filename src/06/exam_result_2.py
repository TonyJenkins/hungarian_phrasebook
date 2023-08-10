#!/usr/bin/env python3

if __name__ == '__main__':

    mark = int(input("Enter the student's mark: "))

    if 0 <= mark <= 100:

        if mark >= 70:
            print('Distinction!')
        elif mark >= 40:
            print('Pass!')
        else:
            print('Fail!')

    else:
        print('Mark out of range')
