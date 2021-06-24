import timeit

COUNT = 100_000

#O(n!)
def f1(i):
    r = [j for j in range(2, COUNT)]
    prime = [2, ]
    for j, v in enumerate(r[1:]):
        flag = 1
        for n in r[:j]:
            if v % n == 0:
                flag = 0
                break
        if flag:
            prime.append(v)
        # if len(prime) > i:
        #     break
    return prime[i]

#O(n)
def f2(i):
    r = [j for j in range(COUNT)]
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
    return res[i]


print(timeit.timeit(f'f1(1_000)', globals=globals(), number=1))
print(timeit.timeit(f'f2(1_000)', globals=globals(), number=1))
