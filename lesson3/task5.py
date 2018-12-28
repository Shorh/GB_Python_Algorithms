# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

size = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(f'Исходный массив: \n{array}')

min_1 = min_2 = float('inf')
for a in array:
    if a < min_1:
        min_1 = a
    elif a < min_2:
        min_2 = a

print(f'Первое минимальное значение :{min_1}')
print(f'Второе минимальное значение :{min_2}')
