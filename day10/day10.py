with open('input.txt') as f:
    lines = f.read().splitlines()

class bot(object):
    def __init__(self, number):
        self.name = 'bot ' + str(number)
        self.min = None
        self.max = None
        self.chips = []
        self.max_to = None
        self.min_to = None


    def set_minmax(self):
        if len(self.chips) > 1:
            self.min = min(self.chips)
            self.max = max(self.chips)

        if len(self.chips) > 2:
            print(f'WHOAAA, I ({self.name}) got 3 (!) chips or more!!!!')


    def follow_order(self, bots, change):
        if self.min is not None and self.min_to is not None:
            if self.min not in bots[self.min_to].chips:
                bots[self.min_to].chips.append(self.min)
                change = True
        if self.max is not None and self.max_to is not None:
            if self.max not in bots[self.max_to].chips:
                bots[self.max_to].chips.append(self.max)
                change = True
        return change


    def __repr__(self):
        string = self.name + ' has ' + str(len(self.chips)) + ' number of chips'
        if self.min:
            string += ', min value ' + str(self.min)
        if self.max:
            string += ', max value ' + str(self.max)
        string2 = ' min goes to ' + str(self.min_to) + ', max goes to ' + str(self.max_to)
        if len(self.chips) > 2:
            string2 += '... How can I have 2+ Chips, WHOAAAA CRAZY!'
        return string + '\n  --> ' + string2


def print_bots(bots):
    lst = list(bots.keys())
    lst.sort()
    for bot in lst:
        print(bots[bot])


def count_chips(bots):
    count = [0, 0, 0]
    for bot in bots.values():
        count[len(bot.chips)] += 1
    print(count)


def min_max_boundary(bots, values):
    # Set min value to bot min and max value to bot max
    max_change = False
    min_change = False
    for bot in bots.values():
        if len(bot.chips) == 1:
            if bot.chips[0] == min(values) and not min_change:
                bot.min = bot.chips[0]
                del values[0]
                min_change = True
            if bot.chips[0] == max(values) and not max_change:
                bot.max = bot.chips[0]
                del values[-1]
                max_change = True
    return max_change, min_change

def iteration(bots, change):
    for cur_bot in bots.values():
        cur_bot.set_minmax()
        change = cur_bot.follow_order(bots, change)
    return change

def update_minmax(bots):
    for bot in bots.values:
        bot.set_minmax()

bots = {}
values = []
bot_pos = [1, 6, -1]

for line in lines:
    if line[0:3] == 'val':
        value = int(line.split(' ')[1])
        number = int(line.split(' ')[-1])
        values.append(value)
        if number not in list(bots.keys()):
            bots[number] = bot(number)
        bots[number].chips.append(value)
    else:
        number = int(line.split(' ')[bot_pos[0]])
        if number not in list(bots.keys()):
            bots[number] = bot(number)
        if line.split(' ')[bot_pos[1] - 1] == 'bot':
            bots[number].min_to = int(line.split(' ')[bot_pos[1]])
        else:
            # output found; use bot class 1xxx series
            pass
        if line.split(' ')[bot_pos[2] - 1] == 'bot':
            bots[number].max_to = int(line.split(' ')[bot_pos[2]])
        else:
            # output found; use bot class 1xxxx series
            pass

values.sort()
min_max_boundary(bots, values)
chip_count = 0
for bot in bots.values():
    bot.set_minmax()
    chip_count += len(bot.chips)

print_bots(bots)
print(f'chip count = {chip_count}')

count = 0
while True:
    change = False
    iteration(bots, change)
    count += 1
    # if not change:
    if count > 200:
        # change_2 = min_max_boundary(bots, values)
        # if not change_2[0] and not change_2[1]:
        print(f'steady state reached after {count} iterations')
        break



## CHECK ITERATION!!! ###
# Check amount of chips per bot
# print(f'\n\n--- printing list of bots ---\n\n')
# print_bots(bots)

chip_count = 0
for bot in bots.values():
    bot.set_minmax()
    chip_count += len(bot.chips)

print_bots(bots)
print(f'chip count = {chip_count}')

found = False
for bot in bots.values():
    if 17 in bot.chips and 61 in bot.chips:
        print(f'bot {bot.name} is the answer')
        found = True

if not found:
    print('Still looking ...')
