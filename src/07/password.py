#!/usr/bin/env python3

import getpass

if __name__ == '__main__':

    try:
        password = getpass.getpass()
        re_entry = getpass.getpass('Re-enter: ')

        user = getpass.getuser()

        if password == re_entry:
            print('User:     ', user)
            print('Password: ', password)
        else:
            print('Passwords did not match.')

    except getpass.GetPassWarning:
        print('Password will show on screen. Exiting!')
