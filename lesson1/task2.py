# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# ​проходящей через эти точки

print('Введите координаты двух точек:')
a_x = int(input('a_x = '))
a_y = int(input('a_y = '))
b_x = int(input('b_x = '))
b_y = int(input('b_y = '))

k = (b_y - a_y) / (b_x - a_x)
b = a_y - a_x * k

print(f'Уравнение прямой, проходящей через данные две точки: y = {k}x + {b}')
