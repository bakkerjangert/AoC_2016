limit = 272
data = '11100010111110100'

# # test data
# limit = 20
# data = '10000'

def dragon(data, limit):
    while len(data) < limit:
        a = data
        b = a[::-1]
        b_new = ''
        for char in b:
            if char == '0':
                b_new += '1'
            elif char == '1':
                b_new += '0'
            else:
                b_new += char
        data = a + '0' + b_new
    return data[0:limit]


def check_sum(string):
    while len(string) % 2 != 1:
        check = ''
        for i in range(len(string) // 2):
            if string[i * 2] == string[i * 2 + 1]:
                check += '1'
            else:
                check += '0'
        print(check)
        string = check
    return string

string = dragon(data, limit)
string = check_sum(string)
print(string)
print(len(string) % 2)


