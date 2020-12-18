from Astar import Astar

with open('input.txt') as f:
    lines = f.read().splitlines()

maze = []
for line in lines:
    maze.append([])
    for char in line:
        maze[-1].append(char)


def print_maze(maze):
    for line in maze:
        print('')
        for char in line:
            print(char, end='')

points = []

i = 0
for line in maze:
    j = 0
    for char in line:
        if char.isdigit():
            points.append([int(char), (j, i)])
            maze[i][j] = '.'
        j += 1
    i += 1

print_maze(maze)
print('\n')
print(points)

lengths = {}
for line in points:
    start = None

# start = points[2][1]
# end = points[0][1]
# path = Astar(maze, start, end)
#
# print(path)
# print(len(path))
#
# # update maze:
# maze[start[1]][start[0]] = 'O'
# for line in path:
#     x = line[0]
#     y = line[1]
#     maze[y][x] = 'A'
# maze[end[1]][end[0]] = 'X'
# print_maze(maze)
