# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

array_size = 30
array_min_num = 0
array_max_num = 1000

random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
max_id = 0
min_id = 0
min_num = random_array[0]
max_num = min_num

print(random_array)

for i, elem in enumerate(random_array):
    if elem > max_num:
        max_id = i
        max_num = elem
    if elem < min_num:
        min_id = i
        min_num = elem

random_array[max_id], random_array[min_id] = random_array[min_id], random_array[max_id]
print(random_array)
