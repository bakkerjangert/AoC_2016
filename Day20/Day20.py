import numpy as np
import pylab as plt
with open('input.txt') as f:
    lines = f.read().splitlines()

start = []
end = []

for line in lines:
    start.append(int(line.split('-')[0]))
    end.append(int(line.split('-')[1]))

# for i in range(len(start)):
#     print(start[i], '-', end[i])

ips = np.array([start, end])
ips = ips.transpose()
ips = np.sort(ips, axis=0)
# print(ips)
# print(len(ips[:,0]))
i = 0

while i + 1 < len(ips[:, 0]):
    print(f'{ips[i + 1, 0]} < {ips[i, 1]} < {ips[i + 1, 1]}')
    if ips[i + 1, 0] <= ips[i, 1] <= ips[i + 1, 1]:
        ips[i, 1] = ips[i + 1, 1]
        ips = np.delete(ips, i + 1, 0)
    elif ips[i + 1, 1] <= ips[i, 1]:
        ips = np.delete(ips, i + 1, 0)
    else:
        i += 1

print(ips)
print(len(ips[:,0]))

print(f'the answer to part 1 is {ips[0, 1] + 1}')

#part b
count = 0
for i in range(len(ips[:,0]) - 1):
    count += (ips[i + 1, 0] - ips[i, 1] - 1)

print(f'the answer to part 2 is {count}')