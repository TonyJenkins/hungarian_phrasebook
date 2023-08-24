#!/usr/bin/env python3


from statistics import mean

NUMBER_OF_MARKS = 5

if __name__ == '__main__':

    marks = []

    for count in range(NUMBER_OF_MARKS):
        next_mark = int(input('Enter the next mark: '))
        marks.append(next_mark)

    print('Average Mark:', mean(marks))
