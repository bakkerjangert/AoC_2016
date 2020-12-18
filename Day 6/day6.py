# Advent of Code 2016 - Day 6 part a
import numpy as np
import pandas as pd
import operator

with open('input.txt') as f:
    lines = f.read().splitlines()

dictionary = {}

for i in range(len(lines[0])):
    dictionary[i] = {}

for line in lines:
    for i in range(len(line)):
        try:
            dictionary[i][line[i]] += 1
        except:
            dictionary[i][line[i]] = 1

max_values = []
min_values = []

for i in range(len(dictionary)):
    print(dictionary[i])
    max_values.append(max(list(dictionary[i].values())))
    min_values.append(min(list(dictionary[i].values())))

answer = ''
answer2 = ''
for i in range(len(dictionary)):
    for k, v in dictionary[i].items():
        if v == max_values[i]:
           answer += k
        if v == min_values[i]:
            answer2 += k

print(f'The answer is {answer}')
print(f'The answer to the 2nd part = {answer2}')
