def upcoming_recipes(count):
    data = '37'
    positions = [0, 1]

    while len(data) < count + 10:
        data += str(int(data[positions[0]]) + int(data[positions[1]]))
        positions[0] = (positions[0] + int(data[positions[0]]) + 1) % len(data)
        positions[1] = (positions[1] + int(data[positions[1]]) + 1) % len(data)

    return data[count:count+10]


def find_pattern(s):
    data = '37'
    positions = [0, 1]

    while s not in data[-len(s)-1:]:
        data += str(int(data[positions[0]]) + int(data[positions[1]]))
        positions[0] = (positions[0] + int(data[positions[0]]) + 1) % len(data)
        positions[1] = (positions[1] + int(data[positions[1]]) + 1) % len(data)
        if len(data) % 1000000 == 0:
            print(len(data))

    return data.index(s)


print('test1', upcoming_recipes(9))
print('test1', upcoming_recipes(5))
print('test1', upcoming_recipes(18))
print('test1', upcoming_recipes(2018))
print('step1', upcoming_recipes('37', 330121))

print('test2', find_pattern('51589'))
print('test2', find_pattern('01245'))
print('test2', find_pattern('92510'))
print('test2', find_pattern('59414'))
print('step2', find_pattern('330121'))
