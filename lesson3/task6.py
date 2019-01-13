# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 100

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]

print(f'Исходная матрица:')
for line in matrix:
    for elem in line:
        print(f'\t{elem}', end='')
    print()

min_ = [float('inf')] * len(matrix[0])
max_min = float('-inf')

# Вариант 1
# for j in range(len(matrix[0])):
#     column = [matrix[i][j] for i in range(len(matrix))]
#     for elem in column:
#         if elem < min_[j]:
#             min_[j] = elem
#     if min_[j] > max_min:
#         max_min = min_[j]

# Вариант 2

for j in range(len(matrix[0])):
    min_[j] = matrix[0][j]

    for i in range(len(matrix)):
        if matrix[i][j] < min_[j]:
            min_[j] = matrix[i][j]

    if min_[j] > max_min:
        max_min = min_[j]

print(f'Минимальные элементы столбцов: {min_}')
print(f'Максимальный элемент среди них: {max_min}')
