# https://drive.google.com/file/d/105N8Kxasy_6hHgWqdWVbnQTcl2NNZ1KE/view?usp=sharing


# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем
# 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Ввести натуральное число: '))
temp_num = num
odd_num = 0
even_num = 0


while temp_num > 0:
    if temp_num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    temp_num //= 10

print(f'В числе {num} четных чисел = {even_num}, а нечетных = {odd_num}')
