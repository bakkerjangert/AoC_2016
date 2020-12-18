# Advent of Code 2016 - Day 7 part a
import numpy as np
import pandas as pd
import operator

with open('input.txt') as f:
    lines = f.read().splitlines()


def find_abba(string):
    if len(string) < 4:
        return False
    for i in range(len(string) - 3):
        if string[i] == string[i + 3] and string[i + 1] == string[i + 2] and string[i] != string[i + 1]:
            return True
    return False


def find_aba(string, bab):
    if len(string) < 3:
        return bab
    for i in range(len(string) - 2):
        if string[i] == string[i + 2] and string[i] != string[i + 1]:
            bab.append(string[i + 1] + string[i] + string[i + 1])
    return bab


def check_bab(string, bab):
    if len(string) < 3:
        return False
    for i in range(len(string) - 2):
        if string[i: i+3] in bab:
            return True
    return False

good_IP = 0
SSL_IP = 0

for line in lines:
    TLS = False
    brackets = []
    non_brackets = []
    string1 = line
    while '[' in string1:
        start = string1.find('[') + 1
        end = string1.find(']')
        brackets.append(string1[start:end])
        string1 = string1[end + 1:]
    string2 = line
    non_brackets.append(string2.split('[')[0])
    start = string2.find('[') + 1
    string2 = string2[start:]
    while '[' in string2:
        start = string2.find(']') + 1
        end = string2.find('[')
        non_brackets.append(string2[start:end])
        string2 = string2[end + 1:]
    non_brackets.append(string2.split(']')[-1])
    # First check if abba outside brackets --> then TLS true
    for string in non_brackets:
        if find_abba(string):
            TLS = True
    # Then check if abba inside brackets --> then TLS false
    for string in brackets:
        if find_abba(string):
            TLS = False
    if TLS:
        good_IP += 1

    # Part 2
    SSL = False
    bab = []
    for string in non_brackets:
        bab = find_aba(string, bab)
    for string in brackets:
        if check_bab(string, bab):
            SSL = True
    if SSL:
        SSL_IP += 1
        
print(f'Number of good ips is {good_IP}')
print(f'Number of SSL ips is {SSL_IP}')
