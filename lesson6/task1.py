# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.
#
# !!!ВНИМАНИЕ!!! Решение добавлены в комменты для каждой функции и в выводы в конце


# import cProfile
import sys
import inspect
from memory_profiler import profile
from collections import deque


# для расчета времени выполнения алгоритма
# N содержит в себе n-значное число в зависимости от IND
N = []
IND = [10, 100, 1000, 10000]
for ind in IND:
    num = [1234567890] * (ind // 10)
    N.append(int("".join(map(str, num))))
MEMORY = {}


def show_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += show_size(key)
                size += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                size += show_size(item)

    return size


# @profile(precision=5)
def reverse(n):
    """
    Рекурсия

    100 loops, best of 3: 2.04 usec per loop      - 10 элементов
    100 loops, best of 3: 44.5 usec per loop      - 100 элементов
    100 loops, best of 3: 1.78 msec per loop      - 1 000 элементов
    RuntimeError                                  - 10 000 элементов

    10/1    0.000    0.000    0.000    0.000 task1.py:30(rev)      - 10 элементов
    91/1    0.000    0.000    0.000    0.000 task1.py:30(rev)      - 100 элементов
    901/1    0.003    0.000    0.003    0.003 task1.py:30(rev)     - 1 000 элементов
    RecursionError                                                 - 10 000 элементов

    потребление памяти - 2 296 байт     - 10 элементов
    """

    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    # @profile(precision=5)
    def rev(a, a_rev):
        for locs in locals().values():
            MEMORY[inspect.stack()[-2][3]] += show_size(locs)

        if a == 0:
            return a_rev
        else:
            return rev(a // 10, a_rev * 10 + a % 10)

    MEMORY[inspect.stack()[0][3]] = 0
    for locs in locals().values():
        MEMORY[inspect.stack()[0][3]] += show_size(locs)

    return rev(n_num, 0)


# @profile(precision=5)
def reverse_loop_1(n):
    """
    Цикл 1

    100 loops, best of 3: 1.26 usec per loop      - 10 элементов
    100 loops, best of 3: 38.7 usec per loop      - 100 элементов
    100 loops, best of 3: 1.45 msec per loop      - 1 000 элементов
    100 loops, best of 3: 117 msec per loop       - 10 000 элементов

    1    0.000    0.000    0.000    0.000 task1.py:51(reverse_loop_1)      - 10 элементов
    1    0.000    0.000    0.000    0.000 task1.py:51(reverse_loop_1)      - 100 элементов
    1    0.001    0.001    0.001    0.001 task1.py:51(reverse_loop_1)      - 1 000 элементов
    1    0.119    0.119    0.119    0.119 task1.py:51(reverse_loop_1)      - 10 000 элементов

    потребление памяти - 76 байт     - 10 элементов
    """

    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    MEMORY[inspect.stack()[0][3]] = 0
    n_rev = 0
    while n_num > 0:
        n_rev = n_rev * 10 + n_num % 10
        n_num = n_num // 10

    for locs in locals().values():
        MEMORY[inspect.stack()[0][3]] += show_size(locs)

    return n_rev


# @profile(precision=5)
def reverse_loop_2(n):
    """
    Цикл 2

    100 loops, best of 3: 1.86 usec per loop      - 10 элементов
    100 loops, best of 3: 7.74 usec per loop      - 100 элементов
    100 loops, best of 3: 117 usec per loop       - 1 000 элементов
    100 loops, best of 3: 2.89 msec per loop      - 10 000 элементов

    1    0.000    0.000    0.000    0.000 task1.py:79(reverse_loop_2)      - 10 элементов
    1    0.000    0.000    0.000    0.000 task1.py:79(reverse_loop_2)      - 100 элементов
    1    0.000    0.000    0.000    0.000 task1.py:79(reverse_loop_2)      - 1 000 элементов
    1    0.003    0.003    0.003    0.003 task1.py:79(reverse_loop_2)      - 10 000 элементов

    потребление памяти - 192 байта     - 10 элементов
    """

    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    MEMORY[inspect.stack()[0][3]] = 0
    n_rev = ''
    n_num = str(n_num)
    for i in n_num:
        n_rev = i + n_rev

    for locs in locals().values():
        MEMORY[inspect.stack()[0][3]] += show_size(locs)

    return int(n_rev)


# @profile(precision=5)
def reverse_slice(n):
    """
    Срезы

    100 loops, best of 3: 0.811 usec per loop      - 10 элементов
    100 loops, best of 3: 1.25 usec per loop       - 100 элементов
    100 loops, best of 3: 18.3 usec per loop       - 1 000 элементов
    100 loops, best of 3: 1.44 msec per loop       - 10 000 элементов

    1    0.000    0.000    0.000    0.000 task1.py:107(reverse_slice)      - 10 элементов
    1    0.000    0.000    0.000    0.000 task1.py:107(reverse_slice)      - 100 элементов
    1    0.000    0.000    0.000    0.000 task1.py:107(reverse_slice)      - 1 000 элементов
    1    0.002    0.002    0.002    0.002 task1.py:107(reverse_slice)      - 10 000 элементов

    потребление памяти - 115 байт   - 10 элементов
    """

    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = str(n_num)[::-1]

    MEMORY[inspect.stack()[0][3]] = 0
    for locs in locals().values():
        MEMORY[inspect.stack()[0][3]] += show_size(locs)

    return int(n_rev)


# @profile(precision=5)
def reverse_deque(n):
    """
    deque

    100 loops, best of 3: 2.49 usec per loop       - 10 элементов
    100 loops, best of 3: 4.86 usec per loop       - 100 элементов
    100 loops, best of 3: 44.3 usec per loop       - 1 000 элементов
    100 loops, best of 3: 1.64 msec per loop       - 10 000 элементов

    1    0.000    0.000    0.000    0.000 task1.py:134(reverse_deque)      - 10 элементов
    1    0.000    0.000    0.000    0.000 task1.py:134(reverse_deque)      - 100 элементов
    1    0.000    0.000    0.000    0.000 task1.py:134(reverse_deque)      - 1 000 элементов
    1    0.002    0.002    0.002    0.002 task1.py:134(reverse_deque)      - 10 000 элементов

    потребление памяти - 1 188 байт   - 10 элементов
    """

    # для расчета времени выполнения алгоритма
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = deque(str(n_num))
    n_rev.reverse()

    MEMORY[inspect.stack()[0][3]] = 0
    for locs in locals().values():
        MEMORY[inspect.stack()[0][3]] += show_size(locs)

    return int(''.join(n_rev))


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
# test_rev(reverse)
# test_rev(reverse_loop_1)
# test_rev(reverse_loop_2)
# test_rev(reverse_slice)
# test_rev(reverse_deque)


# cProfile.run('reverse(3)')
# cProfile.run('reverse_loop_1(3)')
# cProfile.run('reverse_loop_2(3)')
# cProfile.run('reverse_slice(3)')
# cProfile.run('reverse_deque(3)')


# Выводы:
# - рекурсия сдалась на 10 000 элементов
# - Цикл 1 на 100 000 чуть не заставил ноут взлететь
# - Все функции, кроме рекурсии, вызываются 1 раз
# - Лучше всего использовать срезы: у встроенной фунции минимальное время выполнения
# - Если не учитывать срезы и очереди, то оптимальный вариант обрабатывать число как строку и просто менять местами
#   элементы
#
# - OS: macOS Mojave
# - разрядность: 64 бита
# - с точки зрения потребления памяти оптиальный вариант - деление на 10 в цикле
#   (раз переменные внутри цикла не считаем :) )
# - самая кушающая память - рекурсия, за ней - очередь


reverse(0)
reverse_loop_1(0)
reverse_loop_2(0)
reverse_slice(0)
reverse_deque(0)

for name in MEMORY:
    print(f'Функция {name} потребляет {MEMORY[name]} байт памяти под переменные для разворота числа из 10 цифр')
