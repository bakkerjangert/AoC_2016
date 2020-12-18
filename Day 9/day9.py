with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]
decompressed = ''
print(len(string))

while True:
    if string.count('(') == 0:
        decompressed += string
        break
    start = string.find('(')
    end = string.find(')')
    decompressed += string[:start]
    string = string[start:]
    pos = string.find('x')
    char = int(string[1:pos])
    # chars = int(string[1:pos])
    factor = string.split('x')[1]
    factor = int(factor.split(')')[0])
    substring = string[end + 1: end + 1 + char]
    decompressed += substring * factor
    string = string[end + 1 + char:]


print(f'total length = {len(decompressed)}')
print(f'blanks = {decompressed.count(" ")}')



