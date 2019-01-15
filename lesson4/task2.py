# This Python file uses the following encoding: utf-8

# Написать два алгоритма нахождения i-го по счёту простого числа.
# - Без использования Решета Эратосфена;
# - Использовать алгоритм решето Эратосфена

# запуск timeit через терминал:
# python -m timeit -n 100 -s "import task2" "task2.prime(10)"


import cProfile
from math import log
from math import sqrt


# Без использования Решета Эратосфена
def prime(n):
    prime_list = [2]
    len_ = 1
    for i in range(3, int(round(2 * n * log(2 * n))), 2):
        if len_ > n:
            break

        if (i > 10) and (i % 10 == 5):
            continue

        sqrt_ = int((sqrt(i)) + 1)
        for j in prime_list:
            if i % j == 0:
                break
            if j > sqrt_:
                prime_list.append(i)
                len_ += 1
                break
        else:
            prime_list.append(i)
            len_ += 1

    return prime_list[n - 1]


# 100 loops, best of 3: 8.91 usec per loop      - 10 элемент
# 100 loops, best of 3: 149 usec per loop       - 100 элемент
# 100 loops, best of 3: 2.9 msec per loop       - 1 000 элемент
# 100 loops, best of 3: 60.7 msec per loop      - 10 000 элемент


# cProfile.run('prime(10)')
# cProfile.run('prime(100)')
# cProfile.run('prime(1000)')
# cProfile.run('prime(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 task2.py:17(prime)      - 10 элемент
#      1    0.000    0.000    0.000    0.000 task2.py:17(prime)      - 100 элемент
#      1    0.005    0.005    0.005    0.005 task2.py:17(prime)      - 1 000 элемент
#      1    0.071    0.071    0.076    0.076 task2.py:17(prime)      - 10 000 элемент


# Решето Эратосфена
def prime_sieve(n):
    if n == 1:
        return 2

    lst = [i for i in range(int(round(2 * n * log(2 * n))))]
    lst[0] = lst[1] = 0
    len_ = len(lst)
    prime_list = [0 for _ in range(n)]

    k = 0
    for i in lst:
        if i != 0 and k < n:
            prime_list[k] = i
            k += 1
            for j in range(i, len_, i):
                lst[j] = 0

    return prime_list[n - 1]

# 100 loops, best of 3: 13.6 usec per loop      - 10 элемент
# 100 loops, best of 3: 181 usec per loop       - 100 элемент
# 100 loops, best of 3: 3.01 msec per loop      - 1 000 элемент
# 100 loops, best of 3: 79.9 msec per loop      - 10 000 элемент


# cProfile.run('prime_sieve(10)')
# cProfile.run('prime_sieve(100)')
# cProfile.run('prime_sieve(1000)')
# cProfile.run('prime_sieve(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 task2.py:58(prime_sieve)      - 10 элемент
#      1    0.000    0.000    0.000    0.000 task2.py:58(prime_sieve)      - 100 элемент
#      1    0.005    0.005    0.006    0.006 task2.py:58(prime_sieve)      - 1 000 элемент
#      1    0.040    0.040    0.050    0.050 task2.py:58(prime_sieve)      - 10 000 элемент


# def test_prime(func):
#     print(func.__name__)
#     list_in = [1, 10, 100, 1000, 10000]
#     list_out = [2, 29, 541, 7919, 104729]
#     for i, item in enumerate(list_out):
#         assert item == func(list_in[i])
#         print(f'Test {i} OK')
#
#
# test_prime(prime)
# test_prime(prime_sieve)

# Получился алгоритм, работающий чуть быстрее Решета
