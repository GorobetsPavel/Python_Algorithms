# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, надо вывести 6843.

def calculate(number, r_num):
    if number > 10:
        r_num = r_num * 10 + number % 10
        number = number // 10
        return calculate(number, r_num)
    else:
        return r_num * 10 + number


num = int(input('Ввести положительное число: '))
reverse_num = 0
temp_num = num

# while temp_num > 0:
#     reverse_num = reverse_num * 10 + temp_num % 10
#     temp_num = temp_num // 10

# reverse_num = calculate(temp_num, reverse_num)
print(f'Для числа {num}, обратное число - {calculate(temp_num, reverse_num)}')
