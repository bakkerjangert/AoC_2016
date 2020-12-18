# Advent of Code 2016 - Day 2 part a
import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

pad = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                ])

print(pad)
x = 1
y = 1

x_min = 0
x_max = 2
y_min = 0
y_max = 2

password = []
for line in lines:
    for char in line:
        if char == 'U':
            y = max(y - 1, y_min)
        elif char == 'D':
            y = min(y + 1, y_max)
        elif char == 'L':
            x = max(x - 1, x_min)
        elif char == 'R':
            x = min(x + 1, x_max)
    password.append(pad[y, x])
    print(pad[y, x])

key = ''
for item in password:
    key += str(item)

print(f'The code = {key}')
