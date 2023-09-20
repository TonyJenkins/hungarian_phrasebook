#!/usr/bin/env python3

if __name__ == '__main__':

    stringy = input('Enter string to test: ')

    if stringy[0].isupper() and stringy.endswith('.'):
        print('String passes the test.')
    else:
        print('String fails the test.')
