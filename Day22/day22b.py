with open('input.txt') as f:
    lines = f.read().splitlines()

data = []
for line in lines:
    if line[0] != '/':
        continue
    x = line.split('x')[1]
    x = int(x.split('-')[0])
    y = line.split('y')[1]
    y = int(y.split(' ')[0])
    used = line.split('T')[1]
    used = int(used)
    avail = line.split('T')[2]
    avail = int(avail)
    size = used + avail
    try:
        test = data[y]
    except IndexError:
        data.append([])
    data[y].append((size, used, avail))

for line in data:
    print('')
    for point in line:
        print(point[1], end=' ')

print('\n\n----------')
print('Data analyzed --> solution to be found manually in Excel')


