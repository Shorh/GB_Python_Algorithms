# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict


def enterprises(entpr=None):
    enterprise = defaultdict(lambda: [[], ])

    if entpr is None:
        # ввод данных пользователем
        cnt = int(input('Введите количество предприятий: '))
        if cnt == 0:
            return None

        for i in range(1, cnt + 1):
            name = input(f'Введите наименование предприятия {i}: ')
            for j in range(1, 5):
                quarter = int(input(f'Прибыль за {j}-ый квартал = '))
                enterprise[name][0].append(quarter)
    else:
        enterprise = entpr

    profit_average = 0
    for name in enterprise.keys():
        profit = sum(enterprise[name][0])
        enterprise[name].append(profit)
        profit_average += profit

    profit_average /= len(enterprise)

    less_av = []
    more_av = []

    for name in enterprise.keys():
        profit = enterprise[name][1]
        if profit < profit_average:
            less_av.append(name)
        elif profit > profit_average:
            more_av.append(name)

    return more_av, less_av


# Тест работы функции
def test_enterprise(func):
    list_for_dict = [[('Рога', [1, 2, 3, 4]), ('Копыта', [5, 6, 7, 8])],
                     [('Рога', [2, 2, 2, 2]), ('Копыта', [1, 1, 1, 1])],
                     [('Рога', [2, 2, 2, 2]), ('Копыта', [1, 1, 1, 1]), ('Хвост', [1, 1, 2, 3])],
                     [('Рога', [2, 2, 2, 2]), ('Копыта', [1, 1, 1, 1]), ('Хвост', [1, 1, 1, 3])]]
    list_in = []
    for item in list_for_dict:
        dict_in = defaultdict(list)
        for key, value in item:
            dict_in[key].append(value)
        list_in.append(dict_in)

    list_out = [[['Копыта'], ['Рога']],
                [['Рога'], ['Копыта']],
                [['Рога', 'Хвост'], ['Копыта']],
                [['Рога'], ['Копыта']]]
    for i, item in enumerate(list_out):
        assert item[0], item[1] == func(list_in[i])
        print(f'Test {i} OK')


# test_enterprise(enterprises)


# Работа функции по заданному массиву
# ent_list = [('Рога', [2, 2, 2, 2]), ('Копыта', [1, 1, 1, 1]), ('Хвост', [1, 1, 2, 3])]
# ent_dict = defaultdict(list)
# for k, v in ent_list:
#     ent_dict[k].append(v)
#
# more, less = enterprises(ent_dict)

# Работа функции по введенным пользователем данным
try:
    more, less = enterprises()

    more = ', '.join(more)
    less = ', '.join(less)

    print(f'Предприятия, чья прибыль выше среднего по году: {more}')
    print(f'Предприятия, чья прибыль ниже среднего по году: {less}')
except TypeError:
    print('Вы решили не вводить данные')
