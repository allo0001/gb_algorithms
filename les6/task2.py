"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""
import random as rnd
import sys

# размер = 40 + 8 * 100 = 840
ar = [rnd.randint(-100, 100) for _ in range(100)]
print(sys.getsizeof(ar))
max_ = -101
max_i = 0
#print(ar)
for i,n in enumerate(ar):
    if n < 0 and max_ < n:
        max_ = n
        max_i = i

print(f'максимальный отрицательный элемент {max_}, позиция - {max_i}')