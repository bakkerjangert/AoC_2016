# Advent of Code 2016 - Day 2 part a
import numpy as np

def set_lim(xy):
    if xy == 0 or xy == 4:
        return 2
    elif xy == 1 or xy == 3:
        return 1
    elif xy == 2:
        return 0
    else:
        print('unexpected input, check code!')
        exit()

with open('input.txt') as f:
    lines = f.read().splitlines()

pad = np.array([['-', '-', '1', '-', '-'],
                ['-', '2', '3', '4', '-'],
                ['5', '6', '7', '8', '9'],
                ['-', 'A', 'B', 'C', '-'],
                ['-', '-', 'D', '-', '-']])

print(pad)
x = 0
y = 2

x_min = 0
x_max = 4
y_min = 2
y_max = 2

password = []
for line in lines:
    for char in line:
        if char == 'U':
            y = max(y - 1, y_min)
            x_min = set_lim(y)
            x_max = 4 - set_lim(y)
        elif char == 'D':
            y = min(y + 1, y_max)
            x_min = set_lim(y)
            x_max = 4 - set_lim(y)
        elif char == 'L':
            x = max(x - 1, x_min)
            y_min = set_lim(x)
            y_max = 4 - set_lim(x)
        elif char == 'R':
            x = min(x + 1, x_max)
            y_min = set_lim(x)
            y_max = 4 - set_lim(x)
    password.append(pad[y, x])
    print(pad[y, x])

key = ''
for item in password:
    key += str(item)

print(f'The code = {key}')
