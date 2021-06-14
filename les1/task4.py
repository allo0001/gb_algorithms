"""
Написать программу, которая генерирует в указанных пользователем границах
случайное целое число,
случайное вещественное число,
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import time

#print((round(time.time()*1000%15000,2)))
b, e = input('введите диапазон чисел, сиволов или вещественных чисел через пробел: ').split()

if b.isalpha() and e.isalpha():
    len_ = abs(ord(b) - ord(e)) + 1
    print(f'Случайный символ из заданного диапазона - {chr(min(ord(b),ord(e)) + int(time.time()*1000%len_))}')
elif ((b.isdigit() or (b[0] == '-' and b[1:].isdigit))
      and (e.isdigit() or (e[0] == '-' and e[1:].isdigit))):
    b, e = map(int, (b, e))
    len_ = abs(b - e) + 1
    print(f'Случайное число из заданного диапазона - {int(time.time()*1000%len_)}')
elif b.find('.') and e.find('.'):
    b, e = map(float, (b, e))
    len_ = abs(b - e) + 1
    print(f'Случайный символ из заданного диапазона - {round(time.time()*1000%len_,5)}')
