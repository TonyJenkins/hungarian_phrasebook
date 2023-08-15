#!/usr/bin/env python3

from math import sqrt
from random import randint


def place_treasure():
    x_pos = randint(0, 19)
    y_pos = randint(0, 19)

    return x_pos, y_pos


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


def distance_from(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    return sqrt((dx ** 2) + (dy ** 2))


if __name__ == '__main__':

    player_x = 0
    player_y = 0

    treasure_x, treasure_y = place_treasure()

    print('Treasure is at (', treasure_x, ', ', treasure_y, ').', sep='')

    while True:
        print('Player is at (', player_x, ', ', player_y, ').', sep='')
        print('Distance to Treasure: ', distance_from(player_x, player_y, treasure_x, treasure_y))
        next_direction = get_direction()
        player_x, player_y = move(player_x, player_y, next_direction)
