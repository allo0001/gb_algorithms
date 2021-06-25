"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""

import collections

Firm = collections.namedtuple('Firm', ['name', 'q1', 'q2', 'q3', 'q4', 'profit'])

n = int(input('Количество компаний: '))

firms = []

for _ in range(n):
    print(f'{_+1} фирма')
    name = input('Название: ')
    q1 = int(input('Прибыль за 1-ый квартал: '))
    q2 = int(input('Прибыль за 2-ой квартал: '))
    q3 = int(input('Прибыль за 3-й квартал: '))
    q4 = int(input('Прибыль за 4-ый квартал: '))
    profit = q1 + q2 + q3 + q4
    firms.append(Firm(name=name, q1=q1, q2=q2, q3=q3, q4=q4, profit=profit))

p = 0
for f in firms:
    p += f.profit

avg = p / len(firms)
print(f'Средняя прибыль - {avg}')

print('Компании с прибылью выше средней:')
for f in firms:
    if f.profit > avg:
        print(f.name)

print('Компании с прибылью ниже средней:')
for f in firms:
    if f.profit < avg:
        print(f.name)
