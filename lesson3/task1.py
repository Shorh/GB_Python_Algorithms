# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.


START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

# Вариант 1
dct = {i: (END_NUM // i) for i in range(START_DIV, END_DIV + 1)}
print('В диапазоне от 2 до 99 числе, кратных')
for key in dct:
    print(f'{key} - {dct[key]}')

# Вариант 2
# dct = {i: 0 for i in range(START_DIV, END_DIV + 1)}
# for key in dct:
#     j, s = 0, 0
#     while s < END_NUM + 1 - key:
#         s += key
#         j += 1
#     dct[key] = j
# print(dct)
