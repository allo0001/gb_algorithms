"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

ALPHABET = 'abcdefghiklmnopqrstvxyz'

num = int(input('введите номер буквы в алфавите :'))

print(f'Это букава - {ALPHABET[num-1]}')