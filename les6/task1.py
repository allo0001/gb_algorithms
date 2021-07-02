"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
import sys

# размер = 40 + 8 * 98 = 824
a = [i for i in range(2, 100)]
print(sys.getsizeof(a))
# размер = 248 + 24 * 8 = 440
b = {i: 0 for i in range(2, 10)}
print(sys.getsizeof(b))
print(b)

for i in a:
    for j in b.keys():
        if i % j == 0:
            b[j] += 1
print(b)