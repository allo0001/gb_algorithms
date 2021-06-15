"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
import random as rnd

def sum_(n):
    s = 0
    for i in n:
        s += int(i)
    return s

test = [rnd.randint(1, 1000000000) for _ in range(300)]
max_ = 0
for i in test:
    s = sum_(str(i))
    if max_ < s:
        max_ = s

print(f'Максимальная сумма цифр в числе = {max_}')

