# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа: ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a > b:
    if a > c:
        if b > c:
            print(f'Среднее число: {b}')
        else:
            print(f'Среднее число: {c}')
    else:
        print(f'Среднее число: {a}')
else:
    if a > c:
        print(f'Среднее число: {a}')
    else:
        if b > c:
            print(f'Среднее число: {c}')
        else:
            print(f'Среднее число: {b}')
