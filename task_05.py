# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
import string

alphabet = string.ascii_lowercase

letter1 = input('ввести 1-ую строчную английскую букву: ')
letter2 = input('ввести 2-ую строчную английскую букву, отличную от первой: ')

num1 = alphabet.find(letter1) + 1
num2 = alphabet.find(letter2) + 1
num_range = abs(num1 - num2) - 1

print(f'Порядковый номер буквы {letter1} = {num1}')
print(f'Порядковый номер буквы {letter2} = {num2}')
print(f'Количество символов между буквами {letter1} и {letter2} = {num_range}')
