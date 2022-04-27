# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.


import collections

companies = []
comp = collections.namedtuple('comp', 'name, profit_q1, profit_q2, profit_q3, profit_q4, profit')
spam = 0
quan_comp = int(input('Введите количество предприятий: '))

for i in range(quan_comp):
    name = input('Введите наименование предприятия: ')

    profit_q1 = int(input('Введите прибыль за 1 квартала: '))
    profit_q2 = int(input('Введите прибыль за 2 квартала: '))
    profit_q3 = int(input('Введите прибыль за 3 квартала: '))
    profit_q4 = int(input('Введите прибыль за 4 квартала: '))
    profit = profit_q1 + profit_q2 + profit_q3 + profit_q4
    spam += profit
    companies.append(comp(name, profit_q1, profit_q2, profit_q3, profit_q4, profit))

aver = spam / quan_comp

print('Cредняя прибыль за год для всех предприятий: ', aver)

print(f'Предприятия с заработком выше среденего:')
for comp in companies:
    if comp.profit > aver:
        print(f'Компания {comp.name} заработала {comp.profit}')


print(f'Предприятния с заработком ниже среднего:')
for comp in companies:
    if comp.profit < aver:
        print(f'Компания {comp.name} заработала {comp.profit}')
