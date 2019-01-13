# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
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
