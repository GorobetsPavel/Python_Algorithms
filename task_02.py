# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
# 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих
# позициях первого массива стоят четные числа.
import random

array_size = 30
min_num = 0
max_num = 1000

random_array = [random.randint(min_num, max_num) for i in range(array_size)]
new_array =[]

for i, elem in enumerate(random_array):
    if elem % 2 == 0:
        new_array.append(i)

print(f'Для массива: \n {random_array} \n массив с индексами четных позиций \n {new_array}')

