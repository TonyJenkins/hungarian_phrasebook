#!/usr/bin/env python3


from statistics import mean

if __name__ == '__main__':

    marks = []

    while True:
        next_mark = int(input('Enter the next mark (-1 to end): '))
        if next_mark == -1:
            break
        else:
            marks.append(next_mark)

    print('Average Mark:', mean(marks))
