with open('input.txt') as f:
    lines = f.read().splitlines()


def string_split(string):
    char = string.split('x')[0]
    char = int(char[1:])
    factor = string.split('x')[1]
    factor = int(factor.split(')')[0])
    return char, factor


value = 0
string = lines[0]
multiply = []

zeros = ['(', 'x', ')']

for char in string:
    if char.isdigit() or char in zeros:
        multiply.append(0)
    else:
        multiply.append(1)

print(f'len string = {len(string)}, len list = {len(multiply)}')


# Test
# string = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
counter = 0
factors = []
pos_in_original = 0
while True:
    if string.count('(') == 0:
        break
    start = string.find('(')
    end = string.find(')')
    tup = string[start:end + 1]
    chars = tup.split('x')[0]
    chars = int(chars[1:])
    x = tup.split('x')[1]
    x = int(x.split(')')[0])
    tar_char = string[end + 1: end + 1 + chars]
    factors.append((tup, tar_char))
    string = string[end + 1:]
    pos_in_original += end + 1
    for i in range(chars):
        multiply[pos_in_original + i] *= x


for item in factors:
    print(item)

uniques = set(factors)
print(f'{len(factors)}, {len(uniques)}')

print(multiply)
print(f'total length = {sum(multiply)}')
