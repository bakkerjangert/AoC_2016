# Advent of Code 2016 - Day 1 part a

with open('input.txt') as f:
    lines = f.read().splitlines()

directions = lines[0].split(', ')
print(directions)
# Directions --> 0 = N, 1 = E, 2 = S, 3 = W
face = 0


pos = [0, 0]

for item in directions:
    if item[0] == 'R':
        if face < 3:
            face += 1
        else:
            face = 0
    elif item[0] == 'L':
        if face > 0:
            face -= 1
        else:
            face = 3
    steps = int(item[1:])
    if face == 0:
        pos[0] += steps
    elif face == 1:
        pos[1] += steps
    elif face == 2:
        pos[0] -= steps
    elif face == 3:
        pos[1] -= steps

print(f'The position is {pos[0]} North and {pos[1]} East, distance = {abs(pos[0]) + abs(pos[1])}')



