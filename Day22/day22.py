with open('input.txt') as f:
    lines = f.read().splitlines()

viable = 0
for line in lines:
    if line[0] != '/':
        continue
    used = line.split('T')[1]
    used = int(used)
    node_A = line.split('node-')[1]
    node_A = node_A.split(' ')[0]
    if used > 0:
        for line2 in lines:
            if line2[0] != '/':
                continue
            node_B = line2.split('node-')[1]
            node_B = node_B.split(' ')[0]
            if node_A == node_B:
                continue
            avail = line2.split('T')[2]
            avail = int(avail)
            print(f'used = {used}, avail = {avail}')
            if used <= avail:
                viable += 1

print(f'The answer is {viable}')





