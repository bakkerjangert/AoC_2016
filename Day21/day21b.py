with open('input.txt') as f:
    lines = f.read().splitlines()

lines = lines[::-1]


def swap_pos_org(string, x, y):
    if x > y:
        # Swap x and y
        x_temp = x
        x = y
        y = x_temp
    string = string[:x] + string[y] + string[x + 1: y] + string[x] + string[y + 1:]
    return string


def swap_pos(string, x, y):
    # Part two --> No change needed
    # Test passed
    if x > y:
        # Swap x and y
        x_temp = x
        x = y
        y = x_temp
    string = string[:x] + string[y] + string[x + 1: y] + string[x] + string[y + 1:]
    return string


def swap_letter_org(string, x, y):
    new_string = ''
    for char in string:
        if char == x:
            new_string += y
        elif char == y:
            new_string += x
        else:
            new_string += char
    return new_string


def swap_letter(string, x, y):
    # Part b --> No change needed
    # Test passed
    new_string = ''
    for char in string:
        if char == x:
            new_string += y
        elif char == y:
            new_string += x
        else:
            new_string += char
    return new_string


def rot_lr_org(string, x, lr):
    x = x % len(string)  # x might be longer than string
    if lr == 'r':
        x = -x
    string = string[x:] + string[:x]
    return string


def rot_lr(string, x, lr):
    # Part b --> change dir from l to r or viceversa
    # Test passed
    if lr == 'r':
        lr = 'l'
    else:
        lr = 'r'
    x = x % len(string)  # x might be longer than string
    if lr == 'r':
        x = -x
    string = string[x:] + string[:x]
    return string


def rot_pos_org(string, x):
    dir = 'r'
    x = string.find(x)
    if x >= 4:
        x += 1
    x = x + 1
    string = rot_lr_org(string, x, dir)
    return string


def rot_pos(string, x):
    # Part b --> change direction; determine if initial position >= 4
    # Test passed
    #Original shifts {0:1 pos 1, 1:2 pos 3, 2:3 pos 5, 3:4 pos 7, 4:6 pos 10 ==> 2, 5:7 pos 12 ==> 4, 6:8 pos 14 ==> 6, 7:9 ==> 16 pos 0}
    shifts = {0:9, 1:1, 2:6, 3:2, 4:7, 5:3, 6:8, 7:4}
    dir = 'l'
    x = shifts[string.find(x)]
    string = rot_lr_org(string, x, dir)
    return string


def reverse_org(string, x, y):
    if x > y:
        # Swap x and y
        x_temp = x
        x = y
        y = x_temp
    if y + 1 == len(string):
        string1 = string[:x]
        string2 = string[x:]
        string = string1 + string2[::-1]
    else:
        string1 = string[:x]
        string2 = string[x:y+1]
        string3 = string[y+1:]
        string = string1 + string2[::-1] + string3
    return string


def reverse(string, x, y):
    # Part b --> No change needed
    # Test passed
    if x > y:
        # Swap x and y
        x_temp = x
        x = y
        y = x_temp
    if y + 1 == len(string):
        string1 = string[:x]
        string2 = string[x:]
        string = string1 + string2[::-1]
    else:
        string1 = string[:x]
        string2 = string[x:y+1]
        string3 = string[y+1:]
        string = string1 + string2[::-1] + string3
    return string


def move_org(string, x, y):
    if x < y:
        string = string[:x] + string[x + 1:y+1] + string[x] + string[y+1:]
    else:
        string = string[:y] + string[x] + string[y:x] + string[x+1:]
    return string


def move(string, y, x):
    if x < y:
        string = string[:x] + string[x + 1:y+1] + string[x] + string[y+1:]
    else:
        string = string[:y] + string[x] + string[y:x] + string[x+1:]
    return string


code = 'fbgdceah'


# #test
# for char1 in range(len(code)):
#     for char2 in range(len(code)):
#         if char1 == char2:
#             continue
#         check = code
#         print(f'\n-----\nshifting {char1}\n'
#              f'{code}')
#         code = move_org(code, char1, char2)
#         print(code)
#         code = move(code, char1, char2)
#         print(code)
#         print(code == check)
# exit()


for line in lines:
    if line[0:3] == 'swa':
        if line[5:8] == 'pos':
            x = int(line.split(' ')[2])
            y = int(line.split(' ')[-1])
            code = swap_pos(code, x, y)
        else:
            x = line.split(' ')[2]
            y = line.split(' ')[-1]
            code = swap_letter(code, x, y)
    elif line[0:3] == 'rot':
        if line[7:10] == 'bas':
            x = line.split(' ')[-1]
            code = rot_pos(code, x)
        else:
            dir = line[7]
            x = int(line.split(' ')[-2])
            code = rot_lr(code, x, dir)
    elif line[0:3] == 'rev':
        x = int(line.split(' ')[-3])
        y = int(line.split(' ')[-1])
        code = reverse(code, x, y)
    elif line[0:3] == 'mov':
        x = int(line.split(' ')[-4])
        y = int(line.split(' ')[-1])
        code = move(code, x, y)
    else:
        print(f'Line {line} not understood, check code')
        exit()

print(f'The finale code = {code}')