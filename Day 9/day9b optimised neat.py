with open('input.txt') as f:
    lines = f.read().splitlines()

def base_list(string):
    """
    Generates a base list with factor 1 for LETTERS and 0 for (12x345)
    :param string:
    :return:
    """
    list = []
    zeros = ['(', 'x', ')']
    for char in string:
        if char.isdigit() or char in zeros:
            list.append(0)
        else:
            list.append(1)
    return list


def string_split(string):
    """
    Returns amount of characters and factor x as string (chars x factor)
    :param string:
    :return:
    """
    char = string.split('x')[0]
    char = int(char[1:])
    factor = string.split('x')[1]
    factor = int(factor.split(')')[0])
    return char, factor


string = lines[0]
base_list = base_list(string)
pos_in_original = 0

while True:
    if string.count('(') == 0:
        break
    start = string.find('(')
    end = string.find(')')
    tup = string_split(string[start: end + 1])
    chars = tup[0]
    x = tup[1]
    # Update string to next starting position
    string = string[end + 1:]
    pos_in_original += end + 1
    # Multiply targeted characters
    for i in range(chars):
        base_list[pos_in_original + i] *= x


print(f'The total decoded length = {sum(base_list)}')
