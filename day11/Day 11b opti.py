from copy import deepcopy
import numpy as np

# # Start with alternative with only 3 floors (reached after 1 step)? Or is 4th floor required for solution
# layout = [[0, '.', '...', '...', '...', '...'],
#           [1, '.', '...', '...', '...', '...'],
#           [2, '.', '...', '...', '...', '...'],
#           [3, 'E', 'ELG', 'EGM', 'DIG', 'DIM']]

# layout = [[0, '.', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...'],
#           [1, '.', '...', '...', '...', 'COM', '...', 'CUM', '...', 'RUM', '...', 'PLM', '...', '...', '...', '...'],
#           [2, '.', '...', '...', 'COG', '...', 'CUG', '...', 'RUG', '...', 'PLG', '...', '...', '...', '...', '...'],
#           [3, 'E', 'PRG', 'PRM', '...', '...', '...', '...', '...', '...', '...', '...', 'ELG', 'EGM', 'DIG', 'DIM']]
#
names = ['E', 'PRG', 'PRM', 'COG', 'COM', 'CUG', 'CUM', 'RUG', 'RUM', 'PLG', 'PLM', 'ELG', 'EGM', 'DIG', 'DIM']
# Start with alternative with only 3 floors (reached after 1 step)? Or is 4th floor required for solution
layout = np.array([['0', '.', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...'],
                   ['1', '.', '...', '...', '...', 'COM', '...', 'CUM', '...', 'RUM', '...', 'PLM', '...', '...', '...', '...'],
                   ['2', 'E', 'PRG', 'PRM', 'COG', '...', 'CUG', '...', 'RUG', '...', 'PLG', '...', 'ELG', 'EGM', 'DIG', 'DIM']])


initial_moves = 9 # to put eveerything on floor 2
# initial_moves += 32 # from origial part 1 (mind the -1 for startin ong floor 2 instead of 3)

print(f'Initial puzzle input is adjust with {initial_moves} moves to reduce calculation time')

def find_elevator(layout):
    for line in layout:
        if line[1] == 'E':
            return int(line[0])
    return None


def find_eq(layout, floor):
    eq = []
    count = 0
    for item in layout[floor]:
        if count == 0:
            pass
        elif len(item) == 3 and item != '...':
            eq.append(count)
        count += 1
    return eq


def print_LO(layout):
    print('\n--- Printing Layout ---\n')
    for line in layout:
        print(line)


def check_valid(layout):
    chips = []
    protects = []
    for i in range((len(layout[0]) - 2) // 2):
        chips.append(3 + i * 2)
        protects.append(2 + i * 2)
    # Check --> Valid if not other protectors on floor!
    for line in layout:
        for chip in chips:
            prot_needed = False
            if line[chip] != '...':
                for prot in protects:
                    if line[prot] != '...' and prot != chip - 1:
                        prot_needed = True
            if prot_needed:
                if line[chip - 1] == '...':
                    # Chip on floor, but protector not, other gen present
                    return False
    # If all tests have passed
    return True


def check_solution(layout):
    for i in range(len(layout[0]) - 2):
        if layout[0][i + 2] == '...':
            return False
    return True

def encode(layout, names):
    code = ''
    i = 1
    for name in names:
        code += str(layout[:, i].tolist().find(name))
    return code

def gen_2_eq(eq):
    lst = []
    for i in range(len(eq)):
        for j in range(i + 1, len(eq)):
            lst.append((eq[i], eq[j]))
    return lst


def up_one(layout, floor, eq):
    # Move elevator
    layout[floor + 1][1] = 'E'
    layout[floor][1] = '.'
    # Move eq
    layout[floor + 1][eq] = layout[floor][eq]
    layout[floor][eq] = '...'
    return layout


def up_two(layout, floor, eq):
    # Move elevator
    layout[floor + 1][1] = 'E'
    layout[floor][1] = '.'
    # Move eq
    for i in range(2):
        layout[floor + 1][eq[i]] = layout[floor][eq[i]]
        layout[floor][eq[i]] = '...'
    return layout


def down_one(layout, floor, eq):
    # Move elevator
    layout[floor - 1][1] = 'E'
    layout[floor][1] = '.'
    # Move eq
    layout[floor - 1][eq] = layout[floor][eq]
    layout[floor][eq] = '...'
    return layout


def down_two(layout, floor, eq):
    # Move elevator
    layout[floor - 1][1] = 'E'
    layout[floor][1] = '.'
    # Move eq
    for i in range(2):
        layout[floor - 1][eq[i]] = layout[floor][eq[i]]
        layout[floor][eq[i]] = '...'
    return layout


# down_one(layout, 2, 3)
# print_LO(layout)
# print(check_valid(layout))
#
# layout = [[0, '.', '...', '...', '...', '...', '...', '...', '...', '...', '...', '...'],
#           [1, '.', '...', '...', '...', 'COM', '...', 'CUM', '...', 'RUM', '...', 'PLM'],
#           [2, 'E', 'PRG', 'PRM', 'COG', '...', 'CUG', '...', 'RUG', '...', 'PLG', '...']]
# print(check_solution(layout))
# layout = [[0, '.', 'ppp', 'ppp', 'ppp', 'ppp', 'ppp', 'ppp', 'ppp', 'ppp', 'ppp', 'ppp'],
#           [1, '.', '...', '...', '...', 'COM', '...', 'CUM', '...', 'RUM', '...', 'PLM'],
#           [2, 'E', 'PRG', 'PRM', 'COG', '...', 'CUG', '...', 'RUG', '...', 'PLG', '...']]
# print(check_solution(layout))

past_layouts = []
search_tree = [[layout]]
cur_layout = deepcopy(layout)
past_layouts.append(encode(cur_layout, names))
move = 0
# for i in range(4):
while True:
    move += 1
    print(f'\n --- Processing Move {move}')
    print(f'lenght of previous level was {len(search_tree[-1])}')
    solution = False
    search_tree.append([])
    for lay in search_tree[-2]:
        cur_layout = deepcopy(lay)
        floor = find_elevator(cur_layout)
        equipment = find_eq(cur_layout, floor)
        # first do 1 eq movement
        for i in range(len(equipment)):
            if floor > 0:
                new_layout = deepcopy(cur_layout)
                down_one(new_layout, floor, equipment[i])
                if check_valid(new_layout) and encode(new_layout, names) not in past_layouts:
                    search_tree[-1].append(deepcopy(new_layout))
                    past_layouts.append(encode(new_layout, names))
                    if not solution:
                        solution = check_solution(new_layout)
            if floor + 1 < len(cur_layout):
                new_layout_2 = deepcopy(cur_layout)
                up_one(new_layout_2, floor, equipment[i])
                if check_valid(new_layout_2) and encode(new_layout_2, names) not in past_layouts:
                    search_tree[-1].append(deepcopy(new_layout_2))
                    past_layouts.append(encode(new_layout_2, names))
                    if not solution:
                        solution = check_solution(new_layout_2)
        # then do 2 pieces of equipment
        two_eq = gen_2_eq(equipment)
        for i in range(len(two_eq)):
            if floor > 0:
                new_layout_3 = deepcopy(cur_layout)
                down_two(new_layout_3, floor, two_eq[i])
                if check_valid(new_layout_3) and encode(new_layout_3, names) not in past_layouts:
                    search_tree[-1].append(deepcopy(new_layout_3))
                    past_layouts.append(encode(new_layout_3, names))
                    if not solution:
                        solution = check_solution(new_layout_3)
            if floor + 1 < len(cur_layout):
                new_layout_4 = deepcopy(cur_layout)
                up_two(new_layout_4, floor, two_eq[i])
                if check_valid(new_layout_4) and encode(new_layout_4, names) not in past_layouts:
                    search_tree[-1].append(deepcopy(new_layout_4))
                    past_layouts.append(encode(new_layout_4, names))
                    if not solution:
                        solution = check_solution(new_layout_4)
    if solution:
        print(f'Solution found after {move} moves. Add the intial moves, {initial_moves} moves to this number')
        break
    if len(search_tree[-1]) == 0:
        print(f'No more moves after {move} moves. Check the code')
        break




# # for line in search_tree:
# #     print(line)
# #
# print('\n')
# for lay in search_tree[-4]:
#     print_LO(lay)
#     print(check_valid(lay))
#
# print(f'\n --- Solution already found? --- \n')
# print(check_solution(search_tree[-4][2]))
# layout = search_tree[-3][0]
# down_one(layout, 1, 3)
# print_LO(layout)
# print(check_solution(layout))
# # Check step 33 --> search_tree[-3]; it should move up from there but it doesnt????
