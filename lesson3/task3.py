# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

min_i = max_i = 0

for i in range(1, len(array)):
    if array[min_i] > array[i]:
        min_i = i
    elif array[max_i] < array[i]:
        max_i = i

print(f'min = {array[min_i]} на {min_i} позиции')
print(f'max = {array[max_i]} на {max_i} позиции')

array[min_i], array[max_i] = array[max_i], array[min_i]
print(f'Поменяли местами минимальный и максимальный элементы: \n{array}')
