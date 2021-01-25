# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
num1 = float(input('ввести 1-ое число: '))
num2 = float(input('ввести 2-ое число: '))
num3 = float(input('ввести 3-е число: '))

if num1 > num2 > num3 or num1 < num2 < num3:
    print(f'Число {num2} является средним')
elif num3 > num1 > num2 or num3 < num1 < num2:
    print(f'Число {num1} является средним')
else:
    print(f'Число {num3} является средним')