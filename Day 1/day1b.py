# Advent of Code 2016 - Day 1 part a
import pylab as plt


def firstDuplicate(a):
    set_ = set()
    for item in a:
        if item in set_:
            return item
        set_.add(item)
    return None

with open('input (1).txt') as f:
    lines = f.read().splitlines()

directions = lines[0].split(', ')

# Directions --> 0 = N, 1 = E, 2 = S, 3 = W
face = 'N'
faces = ('N', 'E', 'S', 'W')

pos = [0, 0]
pos_visited = []

pos_visited.append(tuple(pos))

for item in directions:
    if item[0] == 'R':
        if face == 'W':
            face = 'N'
        else:
            face = faces[faces.index(face) + 1]
    elif item[0] == 'L':
        face = faces[faces.index(face) - 1]
    steps = int(item[1:])
    if face == 'N':
        for step in range(steps):
            pos[0] += 1
            pos_visited.append(tuple(pos))
    elif face == 'E':
        for step in range(steps):
            pos[1] += 1
            pos_visited.append(tuple(pos))
    elif face == 'S':
        for step in range(steps):
            pos[0] -= 1
            pos_visited.append(tuple(pos))
    elif face == 'W':
        for step in range(steps):
            pos[1] -= 1
            pos_visited.append(tuple(pos))


test_set = []
for item in pos_visited:
    if item in test_set:
        position = item
        break
    test_set.append(item)

# position = firstDuplicate(pos_visited)
print(f'The position is {position[0]} North and {position[1]} East, distance = {abs(position[0]) + abs(position[1])}')

x = []
y = []
for item in pos_visited:
    x.append(item[1])
    y.append(item[0])

plt.plot(x, y)
plt.show()



