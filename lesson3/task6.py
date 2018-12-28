# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

size = 5
min_item = 0
max_item = 100
matrix = [[random.randint(min_item, max_item) for _ in range(size)] for _ in range(size)]

print(f'Исходная матрица:')
for line in matrix:
    for elem in line:
        print(f'\t{elem}', end='')
    print()

min_ = [float('inf')] * len(matrix[0])
max_min = float('-inf')

for j in range(len(matrix[0])):
    column = [matrix[i][j] for i in range(len(matrix))]
    for elem in column:
        if elem < min_[j]:
            min_[j] = elem
    if min_[j] > max_min:
        max_min = min_[j]

print(f'Минимальные элементы столбцов: {min_}')
print(f'Максимальный элемент среди них: {max_min}')
