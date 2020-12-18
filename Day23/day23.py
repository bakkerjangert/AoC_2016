with open('input.txt') as f:
    lines = f.read().splitlines()

reg = [7, 0, 0, 0]
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
        try:
            reg_val = int(line.split(' ')[2])
        except:
            reg_val = reg[regs.index(line.split(' ')[2])]
        if reg_x != 0:
            return reg_val
        return 0
    try:
        reg_val = int(line.split(' ')[2])
    except:
        reg_val = reg[regs.index(line.split(' ')[2])]
    if reg[reg_index] != 0:
        return reg_val
    return 0


def tgl(i, reg, lines, regs=REGS):
    line = lines[i]
    reg_index = regs.index(line.split(' ')[1])
    val = reg[reg_index]
    try:
        line = lines[i + val]
    except IndexError:
        # Targeted line outside program --> Program unchanged
        return lines
    if len(line.split(' ')) == 2:
        if line[0:3] == 'inc':
            line = 'dec' + line[3:]
            lines[i + val] = line
            return lines
        else:
            line = 'inc' + line[3:]
            lines[i + val] = line
            return lines
    elif len(line.split(' ')) == 3:
        if line[0:3] == 'jnz':
            if line[-1].isdigit():
                # Input number, not register; skip line in future
                line = 'SKIP'
                lines[i + val] = line
                return lines
            line = 'cpy' + line[3:]
            lines[i + val] = line
            return lines
        else:
            line = 'jnz' + line[3:]
            lines[i + val] = line
            return lines
    return lines


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
    elif line[0:3] == 'tgl':
        # lines_copy = lines.copy()
        # print(f'\n reg = {reg}')
        # print(f'\n value of i = {i}')
        lines = tgl(i, reg, lines)
        # print('\n--- Printing Lines ---\n')
        # for j in range(len(lines)):
        #     print(f'{lines[j]} ---> {lines_copy[j]}')
        # print(f'\n value of i = {i}')
    i += 1
    print(f'\n value of i = {i}')


print(reg)