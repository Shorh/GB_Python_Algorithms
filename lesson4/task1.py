# This Python file uses the following encoding: utf-8
# так и не поняла до конца, для чего эта строка timeit'у, запущенному через терминал

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# запуск timeit через терминал:
# python -m timeit -n 100 -s "import task1" "task1.reverse(0)"


import cProfile
from collections import deque


# для расчета времени выполнения алгоритма
# N содержит в себе n-значное число в зависимости от IND
N = []
IND = [10, 100, 1000, 10000]
for ind in IND:
    num = [123456789] * (ind // 10)
    N.append(int("".join(map(str, num))))


# Рекурсия
def reverse(n):
    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    def rev(a, a_rev):
        if a == 0:
            return a_rev
        else:
            return rev(a // 10, a_rev * 10 + a % 10)

    return rev(n_num, 0)

# 100 loops, best of 3: 2.04 usec per loop      - 10 элементов
# 100 loops, best of 3: 44.5 usec per loop      - 100 элементов
# 100 loops, best of 3: 1.78 msec per loop      - 1 000 элементов
# RuntimeError                                  - 10 000 элементов

# cProfile.run('reverse(3)')
# 10/1    0.000    0.000    0.000    0.000 task1.py:30(rev)      - 10 элементов
# 91/1    0.000    0.000    0.000    0.000 task1.py:30(rev)      - 100 элементов
# 901/1    0.003    0.000    0.003    0.003 task1.py:30(rev)     - 1 000 элементов
# RecursionError                                                 - 10 000 элементов


# Цикл 1
def reverse_loop_1(n):
    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = 0
    while n_num > 0:
        n_rev = n_rev * 10 + n_num % 10
        n_num = n_num // 10

    return n_rev

# 100 loops, best of 3: 1.26 usec per loop      - 10 элементов
# 100 loops, best of 3: 38.7 usec per loop      - 100 элементов
# 100 loops, best of 3: 1.45 msec per loop      - 1 000 элементов
# 100 loops, best of 3: 117 msec per loop       - 10 000 элементов

# cProfile.run('reverse_loop_1(3)')
#  1    0.000    0.000    0.000    0.000 task1.py:51(reverse_loop_1)      - 10 элементов
#  1    0.000    0.000    0.000    0.000 task1.py:51(reverse_loop_1)      - 100 элементов
#  1    0.001    0.001    0.001    0.001 task1.py:51(reverse_loop_1)      - 1 000 элементов
#  1    0.119    0.119    0.119    0.119 task1.py:51(reverse_loop_1)      - 10 000 элементов


# Цикл 2
def reverse_loop_2(n):
    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = ''
    n_num = str(n_num)
    for i in n_num:
        n_rev = i + n_rev

    return int(n_rev)

# 100 loops, best of 3: 1.86 usec per loop      - 10 элементов
# 100 loops, best of 3: 7.74 usec per loop      - 100 элементов
# 100 loops, best of 3: 117 usec per loop       - 1 000 элементов
# 100 loops, best of 3: 2.89 msec per loop      - 10 000 элементов

# cProfile.run('reverse_loop_2(3)')
# 1    0.000    0.000    0.000    0.000 task1.py:79(reverse_loop_2)      - 10 элементов
# 1    0.000    0.000    0.000    0.000 task1.py:79(reverse_loop_2)      - 100 элементов
# 1    0.000    0.000    0.000    0.000 task1.py:79(reverse_loop_2)      - 1 000 элементов
# 1    0.003    0.003    0.003    0.003 task1.py:79(reverse_loop_2)      - 10 000 элементов


# Срезы
def reverse_slice(n):
    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = str(n_num)[::-1]
    return int(n_rev)

# 100 loops, best of 3: 0.811 usec per loop      - 10 элементов
# 100 loops, best of 3: 1.25 usec per loop       - 100 элементов
# 100 loops, best of 3: 18.3 usec per loop       - 1 000 элементов
# 100 loops, best of 3: 1.44 msec per loop       - 10 000 элементов

# cProfile.run('reverse_slice(3)')
# 1    0.000    0.000    0.000    0.000 task1.py:107(reverse_slice)      - 10 элементов
# 1    0.000    0.000    0.000    0.000 task1.py:107(reverse_slice)      - 100 элементов
# 1    0.000    0.000    0.000    0.000 task1.py:107(reverse_slice)      - 1 000 элементов
# 1    0.002    0.002    0.002    0.002 task1.py:107(reverse_slice)      - 10 000 элементов


# deque
def reverse_deque(n):
    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = deque(str(n_num))
    n_rev.reverse()
    return int(''.join(n_rev))

# 100 loops, best of 3: 2.49 usec per loop       - 10 элементов
# 100 loops, best of 3: 4.86 usec per loop       - 100 элементов
# 100 loops, best of 3: 44.3 usec per loop       - 1 000 элементов
# 100 loops, best of 3: 1.64 msec per loop       - 10 000 элементов

# cProfile.run('reverse_deque(3)')
# 1    0.000    0.000    0.000    0.000 task1.py:134(reverse_deque)      - 10 элементов
# 1    0.000    0.000    0.000    0.000 task1.py:134(reverse_deque)      - 100 элементов
# 1    0.000    0.000    0.000    0.000 task1.py:134(reverse_deque)      - 1 000 элементов
# 1    0.002    0.002    0.002    0.002 task1.py:134(reverse_deque)      - 10 000 элементов


# для проверки работы функции тестом
# def test_rev(func):
#     print(func.__name__)
#     list_in = [1, 2, 3, 4, 5, 6, 7]
#     list_out = [1, 21, 321, 4321, 54321, 654321, 7654321]
#     for i, item in enumerate(list_out):
#         assert item == func(list_in[i])
#         print(f'Test {i} OK')
#
#
# # test_rev(reverse)
# test_rev(reverse_loop_1)
# test_rev(reverse_loop_2)
# test_rev(reverse_slice)
# test_rev(reverse_deque)


# Выводы:
# - рекурсия сдалась на 10 000 элементов
# - Цикл 1 на 100 000 чуть не заставил ноут взлететь
# - Все функции, кроме рекурсии, вызываются 1 раз
# - Лучше всего использовать срезы: у встроенной фунции минимальное время выполнения
# - Если не учитывать срезы, то оптимальный вариант обрабатывать число как строку и просто менять местами элементы
