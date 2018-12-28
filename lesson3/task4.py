# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.

import random

size = 10
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(f'Исходный массив: \n{array}')

max_elem = float('-inf')
max_i = -1

for i in range(len(array)):
    if max_elem < array[i] < 0:
        max_elem = array[i]
        max_i = i

if max_i == -1:
    print('В массиве нет отрицательных элементов')
else:
    print(f'Максимальный отрицальтельный элемент {max_elem} располагается на {max_i}-ой позиции')
