# 4. Определить, какое число в массиве встречается чаще всего.
import random

array_size = 30
array_min_num = 0
array_max_num = 100

random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]

dictionary = dict()
num_of_repetitions = 0
num = random_array[0]

print(random_array)

for elem in random_array:
    if elem in dictionary:
        dictionary[elem] += 1
    else:
        dictionary[elem] = 1

    if num_of_repetitions < dictionary[elem]:
        num_of_repetitions = dictionary[elem]
        num = elem

if num_of_repetitions != 1:
    print(f'Больше всего повторений в массиве у числа {num}, оно встречается {num_of_repetitions} раз')
else:
    print('Все числа массива встречаются по 1 разу.')


