import timeit

#O(2n)
def sum_1(n):
    if n == 1:
        return n
    return n + sum_1(n - 1)

#O(1)
def sum_2(n):
    return n * (n + 1) / 2

#O(N)
def sum_3(n):
    s = 0
    for i in range(n):
        s += i
    return s


print(timeit.timeit(f'sum_1(500)', globals=globals(), number=1000))
print(timeit.timeit(f'sum_2(500)', globals=globals(), number=1000))
print(timeit.timeit(f'sum_3(500)', globals=globals(), number=1000))