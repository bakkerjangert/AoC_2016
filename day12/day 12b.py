with open('input.txt') as f:
    lines = f.read().splitlines()

reg = [0, 0, 1, 0]
REGS = ['a', 'b', 'c', 'd']


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

i = 0
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
    i += 1
    print(f'\n value of i = {i}')
    print(reg)

print(reg)