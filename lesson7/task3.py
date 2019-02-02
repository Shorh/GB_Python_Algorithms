# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы.
#
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

import random

M = 5

SIZE = 2 * M + 1
LEFT = 0
RIGHT = 100

array = [random.randint(LEFT, RIGHT - 1) for _ in range(SIZE)]
# array = [8, 8, 8, 8, 7]
print(f'Исходный массив:\n{array}')


def med(array):
    for i in range(len(array)):
        left = 0
        right = 0
        eq = 0

        for j in range(len(array)):
            if i == j:
                continue
            if array[j] == array[i]:
                eq += 1
            elif array[j] < array[i]:
                left += 1
            elif array[j] > array[i]:
                right += 1
            else:
                raise Exception('Случилось чудо!!!')

        if eq % 2 == 1:
            if left < right:
                left += 1
            elif left > right:
                right += 1

        if left == right:
            return i


med_i = med(array)
print(f'Медиана = {array[med_i]}, элемент с индексом {med_i}')
