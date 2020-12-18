# Advent of Code 2016 - Day 2 part a
import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

triangles = []

triangle1 = []
triangle2 = []
triangle3 = []
for line in lines:
    triangle1.append(int(line.split()[0]))
    triangle2.append(int(line.split()[1]))
    triangle3.append(int(line.split()[2]))
    if len(triangle1) == 3:
        triangle1.sort()
        triangles.append(tuple(triangle1))
        triangle1 = []
        triangle2.sort()
        triangles.append(tuple(triangle2))
        triangle2 = []
        triangle3.sort()
        triangles.append(tuple(triangle3))
        triangle3 = []

possibles = 0
for item in triangles:
    if item[0] + item[1] > item[2]:
        possibles += 1

print(f'There are {possibles} possible triangles')
