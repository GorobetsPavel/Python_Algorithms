from collections import defaultdict
import numpy

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

n = int(input('Ввести количество предприятий: '))
quarter = 4
company_info = defaultdict(list)
all_profit = 0

for i in range(n):
    company_name = input(f'Введите наименование {i+1} организации: ')
    for j in range(quarter):
        profit = int(input(f'Введите сумму прибыли {j+1}-го квартала: '))
        company_info[company_name].append(profit)
        all_profit += profit
    company_info[company_name].append(numpy.mean(company_info[company_name]))


# all_profit = sum(map(sum, company_info.values()))
av_profit = all_profit / n / quarter
low_company = []
top_company = []

for el in company_info:
    company_data = company_info[el]
    if company_data[4] >= av_profit:
        top_company.append(el)
    else:
        low_company.append(el)

print(f'Компании с прибылью выше средней: {top_company} \nКомпании с прибылью ниже средней: {low_company}')