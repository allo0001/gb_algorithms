"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random as rnd

ar = [rnd.randint(0, 100) for _ in range(100)]

min1, min2 = 101, 101

for n in ar:
    if n < min1:
        min2 = min1
        min1 = n
    elif n < min2:
        min2 = n

print(f'1 - {min1}, 2 - {min2}')
