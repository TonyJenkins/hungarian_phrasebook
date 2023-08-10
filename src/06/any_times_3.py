#!/usr/bin/env python3

if __name__ == '__main__':

    while True:
        table = int(input('Enter the table you require (0-12): '))

        if 0 <= table <= 12:
            for table_line in range(13):
                print(table_line, 'x', table, '=', table_line * table)
            break
        else:
            print('Value out of range!')
