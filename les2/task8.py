"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

p = input('Введите последовательность чисел: ')
n = input('Введите искомую цифру: ')

count_ = 0

for i in p:
    if i == n:
        count_ += 1

print(f'Цифра встречается {count_} раз.')