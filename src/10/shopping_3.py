#!/usr/bin/env python3

if __name__ == '__main__':

    try:
        shopping = open('shopping.txt', 'a')

    except (FileNotFoundError, PermissionError,):
        print('Cannot open file to write!')

    else:
        while True:
            new_item = input('What to buy? (END to exit): ')

            if new_item == 'END':
                break

            shopping.write(new_item + '\n')

        shopping.close()
