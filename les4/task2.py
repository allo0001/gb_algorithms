import timeit


def f1(i):
    r = [j for j in range(2, i * 100)]
    prime = [2,]
    for j, v in enumerate(r[1:]):
        flag = 1
        for n in r[:j]:
            if v % n == 0:
                flag = 0
                break
        if flag:
            prime.append(v)
        if len(prime) == i:
            break
    print(prime)
    return prime[i]


def f2(i):
    r = [j for j in range(i * 10)]
    r[1] = 0
    l = len(r)
    m = 2
    while m < l:
        if r[m] != 0:
            j = m * 2
            while j < l:
                r[j] = 0
                j = j + m
        m += 1
    res = [x for x in r if x > 0]
    print(len(res))
    return res[i]

print(f1(10))
print(f2(10))