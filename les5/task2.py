"""
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], 
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
n = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


def sum_16(x1, x2):
    x1 = x1[::-1]
    x2 = x2[::-1]
    res = []
    p = 0
    if len(x1) < len(x2):
        x1, x2 = x2, x1
    
    for i, v in enumerate(x1):
        if len(x2) > i:
            r = n.index(v) + n.index(x2[i])
        else:
            r = n.index(v)

        res.append(n[(r + p) % 16])
        if (r + p)//16 == 1:
            p = 1
        else:
            p = 0
        
    if p == 1:
        res.append('1')
    return res[::-1] 


def count_(x):
    x = x[::-1]
    c = 0
    
    for i, v in enumerate(x):
        c += n.index(v) * (16 ** i)
    return c


def mul_16(x1, x2):
    if len(x1) < len(x2):
        x1, x2 = x2, x1
    c = count_(x2)
    res = ['0']
    for _ in range(c):
        res = sum_16(res, x1)
    return res
        

# a = list(input('первое число: '))
# b = list(input('второе число: '))

a = list('A2')
b = list('C4F')


print(a)
print(b)

print(f'Сумма : {sum_16(a, b)}')
print(f'Произведение : {mul_16(a, b)}')

