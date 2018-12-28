# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(f'Исходный массив: \n{array}')

min_elem = max_elem = array[0]
min_i = max_i = 0

for i in range(1, len(array)):
    if min_elem > array[i]:
        min_elem = array[i]
        min_i = i

    if max_elem < array[i]:
        max_elem = array[i]
        max_i = i

array[min_i], array[max_i] = array[max_i], array[min_i]
print(f'Поменяли местами минимальный и максимальный элементы: \n{array}')
