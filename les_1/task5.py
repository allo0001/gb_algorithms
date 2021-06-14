"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

ALPHABET = 'abcdefghiklmnopqrstvxyz'

a, b = input('введите две буквы через пробел : ').split()

index_a = ALPHABET.find(a) + 1
index_b = ALPHABET.find(b) + 1

print(f'Первая буква на {index_a} месте, а вторая на {index_b}.')
print(f'Между ними {abs(index_a - index_b) - 1} букв.')
