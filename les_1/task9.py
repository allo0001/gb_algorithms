"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

a, b, c = map(int, input('Введите три числа через пробел : ').split())

if b >= a >= c or b <= a <= c:
    print(f'{a} - среднее число')
elif a >= b >= c or a <= b <= c:
    print(f'{b} - среднее число')
else:
    print(f'{c} - среднее число')
