# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это
# число и сумму его цифр.


a_max = 0
s_max = 0

while True:
    a = int(input(f'Введите число:'))
    if a == 0:
        break

    n = a
    s = 0
    while True:
        s += n % 10
        n //= 10
        if n == 0:
            break

    if s > s_max:
        a_max, s_max = a, s

print(f'Число с максимальной суммой цифр = {a_max}')
print(f'Сумма его цифр = {s_max}')
