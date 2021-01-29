# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = int(input('Ввести натуральное число. (0 - выход из цикла): '))
max_num = 0
max_sum = 0

while num != 0:
    temp_num = num
    temp_sum = 0
    while num > 0:
        temp_sum += num % 10
        num = num // 10
    if temp_sum > max_sum:
        max_num = temp_num
        max_sum = temp_sum

    num = int(input('Ввести натуральное число. (0 - выход из цикла): '))

print(f'{max_num} - число с максимальной суммой, равной {max_sum}')