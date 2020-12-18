from copy import deepcopy
discs = [[10, 13],
         [15, 17],
         [17, 19],
         [1, 7],
         [0, 5],
         [1, 3]]


def time_plus(discs, time):
    for disc in discs:
        disc[0] = (disc[0] + time) % disc[1]


def print_disc(discs):
    for disc in discs:
        print(f'{disc} --- {disc[1] - disc[0]}')



# def test_time(discs):
# print_disc(discs)
# for i in range(10):
#     time_plus(discs, 3)
#     print('-' * 10)
#     print_disc(discs)
#
# exit()

time = 0
timestep = 1
i = 0
for disc in discs:
    i += 1
    print(f'\n--- Turning disc {i}')
    print_disc(discs)
    print(f'current time = {time} and timestep = {timestep}')
    test = disc[1] - i
    while test < 0:
        test += disc[1]
    while disc[0] != test:
        time_plus(discs, timestep)
        time += timestep
    timestep *= disc[1]

print(f'\n--- The answer is time {time} ---')







