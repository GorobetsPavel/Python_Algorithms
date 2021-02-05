# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

first_num = deque(input('Ввести 1-ое число в 16-ричной системе исчесления: '))
second_num = deque(input('Ввести 2-ое число в 16-ричной системе исчесления: '))

amount = deque()

if len(second_num) < len(first_num):
    first_num, second_num = second_num, first_num

first_num.reverse()
second_num.reverse()

digit = 0
j = 0
for num in second_num:
    second = nums.index(num)
    if j < len(first_num):
        first = nums.index(first_num[j])
    else:
        first = 0

    sum_nums = first + second + digit
    amount.append(nums[sum_nums % 16])
    if sum_nums >= 16:
        digit = 1
    else:
        digit = 0
    j += 1

if digit == 1:
    amount.append('1')

amount.reverse()
print(''.join(amount))


# first_num.reverse()
# second_num.reverse()
# test_amount = hex(int(''.join(first_num), 16) + int(''.join(second_num), 16))
# print(f'Проверка: {test_amount}')

# Ввести 1-ое число в 16-ричной системе исчесления: 1F81
# Ввести 2-ое число в 16-ричной системе исчесления: 3B4
# 2335

# ABD67F + FFF = ABE67E