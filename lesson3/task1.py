# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

dct = {i: (99 // i) for i in range(2, 10)}
print('В диапазоне от 2 до 99 числе, кратных')
for key in dct:
    print(f'{key} - {dct[key]}')

# 2-й вариант:
# dct = {i: 0 for i in range(2, 10)}
# for key in dct:
#     j, s = 0, 0
#     while s < 100 - key:
#         s += key
#         j += 1
#     dct[key] = j
# print(dct)
