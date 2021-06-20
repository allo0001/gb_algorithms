"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random as rnd

ar = [rnd.randint(0, 100) for _ in range(100)]
max_, min_ = 0, 101
max_i, min_i = -1, -1
print(ar)
for i, n in enumerate(ar):
    if max_ < n:
        max_ = n
        max_i = i
    if min_ > n:
        min_ = n
        min_i = i

if max_i > min_i:
    print(sum(ar[min_i+1:max_i]))
else:
    print(sum(ar[max_i + 1:min_i]))
