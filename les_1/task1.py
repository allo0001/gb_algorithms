"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

n = input('Введите трехзначное число :')

while len(n) != 3 or not n.isdigit():
    n = input('Введите трехзначное число :')

a, b, c = map(int, n)

print(f'Сумма - {a + b + c}')
print(f'Произведение - {a * b * c}')