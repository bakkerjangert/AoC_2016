with open('input.txt') as f:
    lines = f.read().splitlines()

def light_rect(board, tuple):
    for B in range(tuple[1]):
        for A in range(tuple[0]):
            board[B][A] = '#'
    return board

def shift_column(board, tuple):
    column = tuple[0]
    shift = -(tuple[1] % len(board))
    original = []
    for i in range(len(board)):
        original.append(board[i][column])
    new = original[shift:] + original[:shift]
    for i in range(len(board)):
        board[i][column] = new[i]
    return board

def shift_row(board, tuple):
    row = tuple[0]
    shift = -(tuple[1] % len(board[row]))
    original = board[row].copy()
    new = original[shift:] + original[:shift]
    for i in range(len(board[row])):
        board[row][i] = new[i]
    return board

def print_board(board):
    for item in board:
        print(item)
    return None

instructions = []

board = []
A = 50
B = 6
mark = '.'

for i in range(B):
    board.append([])
    for j in range(A):
        board[i].append(mark)

# light_rect(board, (3, 2))
# print_board(board)
# shift_row(board, (1, 51))
# shift_column(board, (3, 2))
# print('\n\n')
# print_board(board)
# exit()

counter = -1
for line in lines:
    if line[0:3] == 'rec':
        counter += 1
        instructions.append([])
        value = line.split(' ')[-1]
        A = int(value.split('x')[0])
        B = int(value.split('x')[-1])
        instructions[counter].append((A, B))
    else:
        # y = row, x = column
        if 'y=' in line:
            instructions[counter].append('y')
        else:
            instructions[counter].append('x')
        number = line.split('=')[-1]
        shift = int(number.split(' by ')[-1])
        number = int(number.split(' by ')[0])
        instructions[counter].append((number, shift))

for line in instructions:
    light_rect(board, line[0])
    for i in range((len(line)) // 2):
        if line[i*2 + 1] == 'y':
            # Shift row
            shift_row(board, line[i*2 + 2])
        else:
            # shift column
            shift_column(board, line[i*2 + 2])

print_board(board)

count = 0
for line in board:
    count += line.count('#')

print(f'The answer is {count}')

for line in board:
    print('')
    for char in line:
        if char == '#':
            print('#', end='')
        else:
            print(' ', end='')
