import hashlib
#         X  Y
limits = (3, 3)
code = 'qljzarfv'
#test
code = 'qljzarfv'
start = (0, 0)
goal = (3, 3)
dir = ('U', 'D', 'L', 'R')

def pr_error():
    print('Something went wrong, postion out of limit --> Check code')
    exit()


def print_paths(paths):
    for k, v in paths.items():
        print(k, v)


def pos(path, start=start, limits=limits):
    position = list(start)
    for char in path:
        if char == 'U':
            position[1] -= 1
            if position[1] < 0:
                pr_error()
        elif char == 'D':
            position[1] += 1
            if position[1] > limits[1]:
                pr_error()
        elif char == 'L':
            position[0] -= 1
            if position[0] < 0:
                pr_error()
        elif char == 'R':
            position[0] += 1
            if position[0] > limits[0]:
                pr_error()
    return tuple(position)


def doors(path, code=code, dir=dir, limits=limits):
    position = pos(path)
    string = hashlib.md5((code + path).encode())
    string = string.hexdigest()
    string = string[:4]
    # print(string)
    # # test
    # string = 'eeee'
    # position = (1, 1)
    # # end test
    doors = []
    i = 0
    for char in string:
        if not char.isdigit() and not char == 'a':
            if (dir[i] == 'U' and position[1] != 0) or (dir[i] == 'D' and position[1] != limits[1]) or (dir[i] == 'L' and position[0] != 0) or (dir[i] == 'R' and position[0] != limits[0]):
                doors.append(dir[i])
        i += 1
    return doors

path = ''
init_doors = doors(path)
paths = {}

for item in init_doors:
    path = item
    paths[path] = doors(path)

lenght = 1
while True:
    cur_paths = paths.copy()
    for key in cur_paths.keys():
        if pos(key) == goal:
            print(f'Vault found in {len(key)} steps')
            print(f'path taken is {key}')
            exit()
        if len(key) == lenght:
            for item in cur_paths.keys():
                for choice in cur_paths[item]:
                    path = item + choice
                    paths[path] = doors(path)
    print('\nPrinting current paths dictionary')
    print_paths(paths)
    lenght += 1

# test = 'abc3231929'
# string = hashlib.md5(test.encode())
# print(string.hexdigest())

# # initiate
# string = hashlib.md5(code.encode())
# decode = string.hexdigest()
#
# print(decode)