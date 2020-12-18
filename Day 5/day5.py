import hashlib


door_ID = 'cxdnnyjw'
counter = 0
find = '00000'
answer = '-' * 8
# test = 'abc3231929'
# string = hashlib.md5(test.encode())
# print(string.hexdigest())

while True:
    check = door_ID + str(counter)
    # print(check)
    string = hashlib.md5(check.encode())
    code = string.hexdigest()
    # print(code[0:5])
    if code[0:5] == find:
        try:
            pos = int(code[5])
        except:
            pos = 99
        if pos < 8 and answer[pos] == '-':
            if pos < 8:
                answer = answer[:pos] + code[6] + answer[pos + 1:]
            else:
                answer = answer[:pos] + code[6]
            print(f'Found new entry, total code = \n{answer}')
    if '-' not in answer:
        break
    counter += 1

print(f'The password is {answer}')