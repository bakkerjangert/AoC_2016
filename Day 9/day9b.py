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

# Test
# string = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
counter = 0
while True:
    if string.count('(') == 0:
        value += len(string)
        break
    # find initial; assume new (...) is always adjacent
    # print(f'1st string = {string}')
    start = string.find('(')
    value += start
    string = string[start:]
    end = string.find(')')
    # print(f'2nd string = {string}, end = {end}')
    char_fact = string_split(string)
    # cut string
    string = string[end + 1:]
    # print(f'3rd string = {string}')
    string = string[:char_fact[0]] * char_fact[1] + string[char_fact[0]:]
    # print(f'4th string = {string}\n')
    counter += 1
    if counter % 10000 == 0:
        print(len(string))

print(f'decrypted length = {value}')
