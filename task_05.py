# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
# к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

array_size = 30
array_min_num = -100
array_max_num = 100

random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
max_id = 0
max_num = 0

print(random_array)

for i, elem in enumerate(random_array):
    if elem < 0:
        if max_num < elem or max_num == 0:
            max_id = i + 1
            max_num = elem

if max_num == 0:
    print('В массиве нет отрицательных чисел.')
else:
    print(f'Максимальный отрицательный элемент массива = {max_num}, позиция в массива = {max_id}')