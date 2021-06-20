"""
Определить, какое число в массиве встречается чаще всего.
"""
import random as rnd

ar = [rnd.randint(0, 100) for _ in range(100)]

el = {i: 0 for i in set(ar)}

for i in ar:
    el[i] += 1

print(max(el.values())) #переделать