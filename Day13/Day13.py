width = 50
height = 50

start = (1, 1)
end = (31, 39)

fav = 1350

maze = []

def func(x, y, fav=fav):
    val = x * x + 3 * x + 2 * x * y + y + y * y
    val += fav
    val = bin(val)
    val = str(val).count('1')
    if val % 2 == 0:
        return '.'
    else:
        return '#'


def print_maze(maze):
    for line in maze:
        print('')
        for char in line:
            print(char, end='')


for h in range(height):
    maze.append([])
    for w in range(width):
        maze[-1].append(func(w, h))

maze[start[1]][start[0]] = 'O'
maze[end[1]][end[0]] = 'X'

print_maze(maze)