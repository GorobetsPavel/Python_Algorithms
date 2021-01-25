# Все блок схемы: https://drive.google.com/file/d/1kCeNdKSlMoXpgB3ZVDUtmsskxj8ET4ak/view?usp=sharing

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
n = int(input('Ввести положительное трехзначное число: '))

d1 = n // 100
d2 = n % 100 // 10
d3 = n % 10

sum = d1 + d2 + d3
mult = d1 * d2 * d3

print(f'Сумма цифр числа {n} = {sum}')
print(f'Произведение цифр числа {n} = {mult}')

