import re
import random
# 373757
# print('Глаза : ' + str(373757 % 6))
# print('Нос : ' + str(373757 % 4))
# print('Рот : ' + str(373757 % 7))
# print(str(373757 % 5))


eyes = '['
nose = '<'
mouth = 'P'

r_smiles = ['[<P', '[<{)', ':-/', '=-P', 'X-{|', ';<)']
input_data_1 = []

for i in range(5):

    input_data_1.append('')
    for d in range(20):
        r_index = random.randint(0, len(r_smiles)-1)
        r_stash = random.randint(0, 1)
        if r_stash == 0:
            input_data_1[i] = input_data_1[i] + r_smiles[r_index]
        else:
            input_data_1[i] = input_data_1[i] + ' ' + r_smiles[r_index]


"""
m = str(input())

pattern = re.compile('[' + eyes + '][' + nose + '][' + mouth + ']')
print(len(pattern.findall(m)))

"""
# [а-яА-Я]*[аоуыэяёюиеАОУЫЭЯЁЮИЕ]{2}

# dop_pattern = re.compile(
#     '')
# print(dop_pattern.findall('Кривошеее существо гуляет по парку'))
# бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ

# m = input().split(' ')

input_data_3 = ['20 + 22 = 42', '20 / 10 = 2',
                '33 - 11 = 22', '55 * 2 = 110', '5 + 0 = 5']


def func(num):
    return (num**2)*4 - 7


my_pattern = re.compile('[-.*+?^${}()|[\]\/]')

for i in range(0, len(input_data_3)):
    m = input_data_3[i].split(' ')
    for i in range(len(m)):
        if (not my_pattern.match(m[i]) and m[i] != '='):
            m[i] = int(m[i])

    for i in range(len(m)):
        if (type(m[i]) == int):
            m[i] = func(m[i])

    for i in range(len(m)):
        print(m[i], end=' ')

    print('\n')
