#!/usr/bin/env python3

from random import randint


def get_direction():

    while True:
        direction = input('Enter direction to move (N/S/E/W): ')
        if len(direction) == 1 and direction in 'NSEW':
            return direction
        else:
            print('Error! Enter one of N/S/E/W.')


def move(x, y, direction):

    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1

    return x, y


if __name__ == '__main__':

    player_x = 0
    player_y = 0

    while True:
        print('Player is at (', player_x, ', ', player_y, ').', sep='')
        next_direction = get_direction()
        player_x, player_y = move(player_x, player_y, next_direction)
