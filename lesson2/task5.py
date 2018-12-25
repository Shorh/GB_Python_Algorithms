# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Введите количество чисел: '))
a = int(input('Введите искомую цифру: '))

count = 0

for i in range(n):
    m = int(input(f'Введите {i + 1} число: '))
    while True:
        if m % 10 == a:
            count += 1
        m //= 10
        if m == 0:
            break

print(f'Цифра {a} в введенной последовательности встречается {count} раз')
