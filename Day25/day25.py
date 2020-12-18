with open('input.txt') as f:
    lines = f.read().splitlines()

reg = [0, 0, 0, 0]
REGS = ('a', 'b', 'c', 'd')


def cpy(reg, line, regs=REGS):
    reg_index = regs.index(line.split(' ')[2])
    reg_val = line.split(' ')[1]
    try:
        reg_val = int(reg_val)
    except:
        ind = REGS.index(reg_val)
        reg_val = reg[ind]
    reg[reg_index] = reg_val


def inc(reg, line, regs=REGS):
    reg_index = regs.index(line.split(' ')[1])
    reg[reg_index] += 1


def dec(reg, line, regs=REGS):
    reg_index = regs.index(line.split(' ')[1])
    reg[reg_index] -= 1


def jnz(reg, line, regs=REGS):
    try:
        reg_index = regs.index(line.split(' ')[1])
    except:
        reg_x = int(line.split(' ')[1])
        reg_val = int(line.split(' ')[2])
        if reg_x != 0:
            return reg_val
        return 0
    reg_val = int(line.split(' ')[2])
    if reg[reg_index] != 0:
        return reg_val
    return 0

test = 0
counter = 0
while True:
    reg = [test, 0, 0, 0]
    output = []
    i = 0
    steps = 0
    found = False
    while i < len(lines):
        line = lines[i]
        if line[0:3] == 'cpy':
            cpy(reg, line)
            line = lines[i]
        elif line[0:3] == 'inc':
            inc(reg, line)
        elif line[0:3] == 'dec':
            dec(reg, line)
        elif line[0:3] == 'jnz':
            val = jnz(reg, line)
            if val != 0:
                i += val
                continue
        elif line[0:3] == 'out':
            output.append(str(reg[1]))
            if len(output) > 1 and not (output[-1] + output[-2] == '10' or output[-1] + output[-2] == '01'):
                # print(output)
                # print(output[-1] + output[-2])
                # print('Error in sequence')
                # breakpoint()
                break
        i += 1
        steps += 1
        counter += 1
        if counter % 1000 == 0:
            print(f'\n value of i = {i}, testing int = {test}')
            print(f'Value of step = {steps}')
            print(f'Found code = {output}')
        if len(output) > 1000:
            found = True
            break

    if found:
        print(f'The answer is {test}')
        exit()
    test += 1
