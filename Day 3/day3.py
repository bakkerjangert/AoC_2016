# Advent of Code 2016 - Day 2 part a
import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

triangles = []

for line in lines:
    triangle = []
    for i in range(3):
        triangle.append(int(line.split()[i]))
    triangle.sort()
    triangles.append(triangle)

possibles = 0
for item in triangles:
    if item[0] + item[1] > item[2]:
        possibles += 1

print(f'There are {possibles} possible triangles')
