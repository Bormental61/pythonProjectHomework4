# 30. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤ 10^{-10}

# my var
# from math import pi
# d = input("Введите точность отображения числа Пи, число 10^{-1} ≤ d ≤ 10^{-10} : ")
# round_lenth = len(d.split('.')[1])
# print('Число Пи с заданной точностью', d, 'равно', round(pi, round_lenth))

# var1
# from math import pi
# d = input()
# accur = len(d)
# print(str(pi)[0:accur])

# ________________________________________________________________________
# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# my var
# num = int(input("Введите число: "))
# list_simples = [1]
# for i in range(2, num + 1):
#     if not num % i:
#         for j in range(2, (i // 2 + 1)):
#             if not i % j:
#                 break
#         else:
#             list_simples.append(i)
# print(list_simples)

# optimal var
# number_set = set()
# out_list = []
# some_list = list(map(int, input().split()))
# for ind in range(0, len(some_list)):
#     if some_list[ind] not in number_set:
#         number_set.add(some_list[ind])
#         for ind1 in range(ind + 1, len(some_list)):
#             if some_list[ind] == some_list[ind1]:
#                 break
#         else:
#             out_list.append(some_list[ind])
# print(out_list)

# _____________________________________________________________________
# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# user_list = list(map(int, input("Введите числа через пробел: ").split()))
# new_list = []
# for i in user_list:
#     if user_list.count(i) == 1:
#         new_list.append(i)
# print(new_list)

# ________________________________________________________________________
# 33. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#
# import random
# indexes = {2: '\u00B2',
#            3: '\u00B3',
#            4: '\u2074',
#            5: '\u2075',
#            6: '\u2076',
#            7: '\u2077',
#            8: '\u2078',
#            9: '\u2079'}
# k = random.randint(2, 9)
# print(f'Для k = {k}')
# ml = [random.randint(0, 100) for i in range(k + 1)]
# mn = []
# for i in range(len(ml)):
#     if i != len(ml) - 1 and ml[i] != 0 and i != len(ml) - 2:
#         mn.append(f'{ml[i]}x{indexes.get(len(ml) - i - 1)}')
#     elif i == len(ml) - 2 and ml[i] != 0:
#         mn.append(f'{ml[i]}x')
#     elif i == len(ml) - 1 and ml[i] != 0:
#         mn.append(f'{ml[i]}')
# mn = ' + '.join(mn)
# mn += ' = 0'
# print(mn)
# with open('file33.txt', 'w', encoding='utf-8') as data:
#     data.write(f'Для k = {k}\n')
#     data.write(mn)

# ____________________________________________________________________________
# 35. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

indexes = {2: '\u00B2',
           3: '\u00B3',
           4: '\u2074',
           5: '\u2075',
           6: '\u2076',
           7: '\u2077',
           8: '\u2078',
           9: '\u2079'}


def generate_polynomial(k):
    ml = [random.randint(0, 9) for i in range(k + 1)]
    print(ml)
    mn = []
    for i in range(len(ml)):
        if i != len(ml) - 1 and ml[i] != 0 and i != len(ml) - 2:
            mn.append(f'{ml[i]}x{indexes.get(len(ml) - i - 1)}')
        elif i == len(ml) - 2 and ml[i] != 0:
            mn.append(f'{ml[i]}x')
        elif i == len(ml) - 1 and ml[i] != 0:
            mn.append(f'{ml[i]}')
    mn = ' + '.join(mn)
    mn += ' = 0'
    return mn

pn1 = generate_polynomial(random.randint(2, 9))
pn2 = generate_polynomial(random.randint(2, 9))
print(pn1)
print(pn2)
with open('file35_pn1.txt', 'w', encoding='utf-8') as data:
    data.write(pn1)
with open('file35_pn2.txt', 'w', encoding='utf-8') as data:
    data.write(pn2)
with open('file35_res.txt', 'w', encoding='utf-8') as data:
    data.write(f'({pn1.removesuffix(" = 0")}) + ({pn2.removesuffix(" = 0")})')

