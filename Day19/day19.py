players = 3017957

# initiate uneven:
elfs = []
for elf in range(players):
      elfs.append(elf)

while len(elfs) > 1:
    last_entry = []
    if len(elfs) % 2 != 0:
        # Store last elf to make sequence even
        last_entry.append(elfs[-1])
        elfs = elfs[:-1]
    # Cut every 2nd elf
    elfs = elfs[::2]
    if len(last_entry) == 1:
        # Add stored elf at beginning again
        elfs.insert(0, last_entry[0])

# Reminder --> Elfs game starts at elf == 1; not 0 --> add 1 to answer!
print(f'The answer is elf {elfs[0] + 1}')
# print(2**24)
# print(players)

