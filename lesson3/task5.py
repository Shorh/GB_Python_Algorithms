# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: \n{array}')

if array[0] < array[1]:
    min_1, min_2 = 0, 1
else:
    min_1, min_2 = 1, 0

for i in range(2, len(array)):
    if array[i] < array[min_1]:
        spam = min_1
        min_1 = i
        if array[spam] < array[min_2]:
            min_2 = spam

    elif array[i] < array[min_2]:
        min_2 = i

print(f'Первое минимальное значение: {array[min_1]} на {min_1} позиции')
print(f'Второе минимальное значение: {array[min_2]} на {min_2} позиции')
