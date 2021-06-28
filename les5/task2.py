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
            res.append(n[r % 16 + p])
            if r//16 == 1:
                p = 1
            else:
                p = 0
        else:
            res.append(n[n.index(v) + p])
    return res[::-1] 
        

# a = list(input('первое число: '))
# b = list(input('второе число: '))

a = list('A2')
b = list('C4F')

print(a)
print(b)

print(f'Сумма : {sum_16(a, b)}')


