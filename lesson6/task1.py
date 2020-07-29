# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.


import sys
import inspect
from memory_profiler import profile
from collections import deque


# N содержит в себе n-значное число в зависимости от IND
N = []
IND = [10, 100, 1000, 10000]
for ind in IND:
    num = [1234567890] * (ind // 10)
    N.append(int("".join(map(str, num))))

memory = {}


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
    потребление памяти - 2 296 байт     - 10 элементов
    """

    # для расчета объема выделяемой памяти
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    # @profile(precision=5)
    def rev(a, a_rev):
        for locs in locals().values():
            memory[inspect.stack()[-2][3]] += show_size(locs)

        if a == 0:
            return a_rev
        else:
            return rev(a // 10, a_rev * 10 + a % 10)

    memory[inspect.stack()[0][3]] = 0
    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return rev(n_num, 0)


# @profile(precision=5)
def reverse_loop_1(n):
    """
    Цикл 1
    потребление памяти - 76 байт     - 10 элементов
    """

    # для расчета объема выделяемой памяти
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    memory[inspect.stack()[0][3]] = 0
    n_rev = 0
    while n_num > 0:
        n_rev = n_rev * 10 + n_num % 10
        n_num = n_num // 10

    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return n_rev


# @profile(precision=5)
def reverse_loop_2(n):
    """
    Цикл 2
    потребление памяти - 192 байта     - 10 элементов
    """

    # для расчета объема выделяемой памяти
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    memory[inspect.stack()[0][3]] = 0
    n_rev = ''
    n_num = str(n_num)
    for i in n_num:
        n_rev = i + n_rev

    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return int(n_rev)


# @profile(precision=5)
def reverse_slice(n):
    """
    Срезы
    потребление памяти - 115 байт   - 10 элементов
    """

    # для расчета объема выделяемой памяти
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = str(n_num)[::-1]

    memory[inspect.stack()[0][3]] = 0
    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return int(n_rev)


# @profile(precision=5)
def reverse_deque(n):
    """
    deque
    потребление памяти - 1 188 байт   - 10 элементов
    """

    # для расчета объема выделяемой памяти
    n_num = N[n]

    # для проверки работы функции тестом
    # n_num = [i + 1 for i in range(n)]
    # n_num = int("".join(map(str, n_num)))

    n_rev = deque(str(n_num))
    n_rev.reverse()

    memory[inspect.stack()[0][3]] = 0
    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

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


# Выводы:
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

for name in memory:
    print(f'Функция {name} потребляет {memory[name]} байт памяти под переменные для разворота числа из 10 цифр')
