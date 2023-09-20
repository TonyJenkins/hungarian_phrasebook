#!/usr/bin/env python3


from statistics import mean

if __name__ == '__main__':

    marks = []

    while True:
        next_mark = input('Enter the next mark ("Enter" to end): ')
        if not next_mark:
            break
        else:
            marks.append(int(next_mark))

    print('Average Mark:', mean(marks))
