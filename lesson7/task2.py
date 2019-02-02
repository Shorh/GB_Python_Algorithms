# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
from collections import deque
import itertools

SIZE = 10
LEFT = 0
RIGHT = 50

array = [random.uniform(LEFT, RIGHT - 1) for _ in range(SIZE)]
# array = [random.randint(LEFT, RIGHT - 1) for _ in range(SIZE)]
print(f'Исходный массив:\n{array}')


def merge_sort(sort_array):
    if len(sort_array) <= 1:
        return sort_array

    new_size = len(sort_array) // 2

    left = deque(itertools.islice(sort_array, 0, new_size))
    right = deque(itertools.islice(sort_array, new_size, len(sort_array)))

    left = merge_sort(left)
    right = merge_sort(right)

    for k in range(len(sort_array)):
        if len(left) == 0:
            sort_array[k] = right.popleft()
        elif len(right) == 0:
            sort_array[k] = left.popleft()
        else:
            if left[0] <= right[0]:
                sort_array[k] = left.popleft()
            else:
                sort_array[k] = right.popleft()

    return sort_array


print(f'Отсортированный массив:\n{merge_sort(array)}')
