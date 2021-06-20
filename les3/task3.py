"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random as rnd

ar = [ rnd.randint(0, 100) for _ in range(10)]

print(ar)

max_, min_ = 0, 101
max_i, min_i = -1, -1
for i, n in enumerate(ar):
    if max_ < n:
        max_ = n
        max_i = i
    if min_ > n:
        min_ = n
        min_i = i

ar[max_i], ar[min_i] = ar[min_i], ar[max_i]

print(ar)