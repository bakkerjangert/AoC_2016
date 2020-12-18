# Advent of Code 2016 - Day 2 part a
import numpy as np
import pandas as pd
import operator

with open('input.txt') as f:
    lines = f.read().splitlines()

letters = []
IDs = []
checksum = []

for line in lines:
    chk = line.split('[')[-1]
    chk = chk.split(']')[0]
    checksum.append(chk)
    ID = line.split('-')[-1]
    ID = ID.split('[')[0]
    IDs.append(int(ID))
    index = line.rfind('-')
    letters.append(line[:index])

answer = 0
for i in range(len(letters)):
    print(f'\n--- Next Room ---\n')
    counts = {}
    for letter in letters[i]:
        try:
            counts[letter] += 1
        except KeyError:
            counts[letter] = 1
    del counts['-']

    # Create a list of tuples sorted by index 1 i.e. value field
    # list_of_tuples = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # # Iterate over the sorted sequence
    # for elem in list_of_tuples:
    #     print(elem[0], " ::", elem[1])

    letter_sorted = sorted(counts.items(), key=operator.itemgetter(0))
    sorted_list = sorted(letter_sorted, key=operator.itemgetter(1), reverse=True)

    for elem in sorted_list:
        print(elem)

    check_string = ''
    for j in range(5):
        check_string = check_string + sorted_list[j][0]
    print(check_string, checksum[i], IDs[i])
    if check_string == checksum[i]:
        answer += IDs[i]

print(f'\n The answer = {answer}')





