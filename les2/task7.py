"""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""
import random as rnd


def sum_(n):
    if n == 1:
        return n
    return n + sum_(n - 1)


test = [rnd.randint(1, 1000) for _ in range(100)]

for n in test:
    if sum_(n) == n * (n + 1) / 2:
        print(f'Для {n=} равенство выполняется')
    else:
        print(f'Для {n=} равенство не выполняется')
