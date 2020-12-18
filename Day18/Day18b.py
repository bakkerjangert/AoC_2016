with open('input.txt') as f:
    lines = f.read().splitlines()

# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.

def trap(string):
    if string[0] == string[1] == '^' and string[2] == '.':
        return '^'
    if string[1] == string[2] == '^' and string[0] == '.':
        return '^'
    if string.count('^') == 1 and (string[0] == '^' or string[2] == '^'):
        return '^'
    return '.'

len_row = len(lines[0])
total_rows = 400000
counter = 0
for i in range(total_rows - 1):
    cur_row = lines[i]
    new_row = ''
    for j in range(len(cur_row)):
        if j == 0:
            string = '.' + cur_row[:2]
        elif j < len(cur_row) - 1:
            string = cur_row[j - 1: j + 2]
            # print('cause 2')
        else:
            string = cur_row[-2:] + '.'
            # print('cause 3')
        # print(string)
        new_row += trap(string)
    lines.append(new_row)
    if counter % 1000 == 0:
        print(f'at iteration {counter}')
    counter += 1

    # print('END OF LOOP')
    # exit()

counts = 0
for line in lines:
    print(line)
    counts += line.count('.')

print(f'\n the answer is {counts}')


