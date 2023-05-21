import numpy as np
import os


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def cs():
    clear_screen()


def convert_to_2d(array, rows=3):
    return np.reshape(array, (rows, -1))
    # array = list(array)
    # result = []
    # row_len = len(array)//3
    # for _ in range(rows):
    #     result.append(array[0:row_len])
    #     array = array[row_len:]
    # return result


def convert_to_1d(array):
    return np.reshape(array, (1, -1))[0]
    # return array.flatten()


def print_2d(array):
    for row in array:
        print(row)


def convert_to_np(array):
    result = np.array(array)
    return result


# box drawing chars
UPPER_LEFT = '\u250f'
UPPER_RIGHT = '\u2513'
LOWER_LEFT = '\u2517'
LOWER_RIGHT = '\u251b'
VERTICAL_CHAR = '\u2503'
HORIZONTAL_CHAR = '\u2501'
VERTICAL_RIGHT = '\u2523'
VERTICAL_LEFT = '\u252b'
HORIZONTAL_DOWN = '\u2533'
HORIZONTAL_UP = '\u253b'
CROSS_CHAR = '\u254b'
Full_BLOCK_CHAR = '\u2588'
ul = UPPER_LEFT
ur = UPPER_RIGHT
ll = LOWER_LEFT
lr = LOWER_RIGHT
v = VERTICAL_CHAR
h = HORIZONTAL_CHAR
vr = VERTICAL_RIGHT
vl = VERTICAL_LEFT
hd = HORIZONTAL_DOWN
hu = HORIZONTAL_UP
cross = CROSS_CHAR


# game chars
MOON_CHAR = '\u263e'
# SUN_CHAR = '\u2600'
SUN_CHAR = '\u263c'
BLANK_CHAR = '\u2588'
# SUN_CHAR = 'S'
# MOON_CHAR = 'M'
BLANK_CHAR = ' '
