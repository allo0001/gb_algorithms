"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random as rnd


m = [[rnd.randint(0, 50) for j in range(5)] for i in range(5)]

print(*m, sep='\n')

max_ = -1
res = []

for i in range(len(m[0])):
    min_ = 51
    for j in range(len(m)):
        if m[j][i] < min_:
            min_ = m[j][i]
    res.append(min_)
    
print('*' * 20, '\n', res)

for i in res:
    if i > max_:
        max_ = i
        
print('*' * 20)    
print(f'максимальный элемент среди минимальных элементов столбцов матрицы - {max_}')
        
        
        