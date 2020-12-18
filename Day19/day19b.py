from collections import deque

players = 3017957
def rotate(l, n):
    return l[n:] + l[:n]
# initiate uneven:
elfs = []
for elf in range(players):
      elfs.append(elf)

# test = [1, 2, 3]
# print(rotate(test, 1))
# exit()

while len(elfs) > 1:
    num_elfs = len(elfs)
    target = len(elfs) // 2
    if len(elfs) % 2 == 0:
        half = len(elfs) // 2
        elfs = elfs[: half] + elfs[half + 2::3]
        shift = num_elfs - len(elfs)
        elfs = rotate(elfs, shift)
    elif len(elfs) % 2 == 1:
        half = len(elfs) // 2
        elfs = elfs[: half] + elfs[half + 1::3]
        shift = num_elfs - len(elfs)
        elfs = rotate(elfs, shift)
    print(elfs)

# Reminder --> Elfs game starts at elf == 1; not 0 --> add 1 to answer!
print(f'The answer is elf {elfs[0] + 1}')

