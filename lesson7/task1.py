# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

SIZE = 10
LEFT = -100
RIGHT = 100

array = [random.randint(LEFT, RIGHT - 1) for _ in range(SIZE)]
print(f'Исходный массив:\n{array}')


def bubble_sort(array):
    flag = True
    for n in range(1, len(array)):
        if not flag:
            break

        flag = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
        #     print(array)
        # print()


bubble_sort(array)
print(f'Отсортированный по убыванию массив:\n{array}')
