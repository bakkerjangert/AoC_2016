import hashlib

salt = 'cuanljph'

# test = 'abc3231929'
# string = hashlib.md5(test.encode())
# print(string)
# print(string.hexdigest())
#
# exit()

keys = 0
i = 0
test = []
while True:
    string = hashlib.md5((salt + str(i)).encode())
    search = string.hexdigest()
    for j in range(len(search) - 2):
        if search[j] == search[j + 1] == search[j + 2]:
            test.append([])
            test[-1].append(search[j])
            test[-1].append(0)
            test[-1].append(i)
            # print(test)
            break
    k = 0
    while k < len(test) and len(test) > 0:
        key_found = False
        if test[k][1] != 0:
            for l in range(len(search) - 4):
                if search[l] == search[l + 1] == search[l + 2] == search[l + 3] == search[l + 4] == test[k][0]:
                    keys += 1
                    print(f'key {keys} found at position {test[k][2]}')
                    if keys > 63:
                        print(f'\n--- Analyses finished, key 64 found with index {test[k][2]} ---')
                        exit()
                    del test[k]
                    key_found = True
                    break
        if key_found:
            continue
        test[k][1] += 1
        if test[k][1] > 1000:
            del test[k]
            continue
        k += 1
    i += 1
    if keys > 63:
        print(f'Analyses finished, key 64 found with index {test[-1][2]}')
        break
