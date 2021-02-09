# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Взял задачу из 3 практического задания №3. Как раз делал там с лишними переменными.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import sys


def find_min_max_id(_array, max_num, min_num, i, array_len, max_id, min_id):
    if _array[i] > max_num:
        max_num = _array[i]
        max_id = i
    if _array[i] < min_num:
        min_num = _array[i]
        min_id = i
    if i == array_len:
        mem = sys.getsizeof(max_num) + sys.getsizeof(max_id) + sys.getsizeof(min_num) + sys.getsizeof(min_id) \
            + sys.getsizeof(i) + sys.getsizeof(array_len)
        return min_id, max_id, mem
    else:
        return find_min_max_id(_array, max_num, min_num, i + 1, array_len, max_id, min_id)


def main_v_01(_array):
    # random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
    # print(random_array)
    max_id = 0
    min_id = 0
    min_num = _array[0]
    max_num = min_num

    for i, elem in enumerate(_array):
        if elem > max_num:
            max_id = i
            max_num = elem
        if elem < min_num:
            min_id = i
            min_num = elem

    _array[max_id], _array[min_id] = _array[min_id], _array[max_id]
    return sys.getsizeof(max_num) + sys.getsizeof(max_id) + sys.getsizeof(min_num) + sys.getsizeof(min_id) \
        + sys.getsizeof(i) + sys.getsizeof(elem)
    # print(random_array)


def main_v_02(_array):  # without_num
    max_id = 0
    min_id = 0

    for i in range(len(_array)):
        if _array[i] > _array[max_id]:
            max_id = i
        if _array[i] < _array[min_id]:
            min_id = i

    _array[max_id], _array[min_id] = _array[min_id], _array[max_id]
    return sys.getsizeof(max_id) + sys.getsizeof(min_id) + sys.getsizeof(i)


def main_v_03(_array):   # _recursion
    id_min_max = find_min_max_id(_array, _array[0], _array[0], 1, len(_array) - 1, 0, 0)
    min_id = id_min_max[0]
    max_id = id_min_max[1]

    _array[max_id], _array[min_id] = _array[min_id], _array[max_id]
    return sys.getsizeof(max_id) + sys.getsizeof(min_id) + sys.getsizeof(id_min_max) + sys.getsizeof(id_min_max[2])


def main_v_04(_array):     # min() max()
    # random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
    min_num = min(_array)
    max_num = max(_array)
    max_id = _array.index(max_num)
    min_id = _array.index(min_num)
    _array[max_id], _array[min_id] = _array[min_id], _array[max_id]
    return sys.getsizeof(max_id) + sys.getsizeof(min_id)


common_memory = 0
array_min_num = 0
common_memory += sys.getsizeof(array_min_num)
array_max_num = 1000
common_memory += sys.getsizeof(array_max_num)
random_array = [random.randint(array_min_num, array_max_num) for i in range(20)]
print(random_array)
common_memory += sys.getsizeof(random_array)

print(f'Для 1 решения требуется {common_memory + main_v_01(random_array)} памяти.')
print(f'Для 2 решения требуется {common_memory + main_v_02(random_array)} памяти.')
print(f'Для 3 решения требуется {common_memory + main_v_03(random_array)} памяти.')
print(f'Для 4 решения требуется {common_memory + main_v_04(random_array)} памяти.')
#
# Для 1 решения требуется 236 памяти.
# Для 2 решения требуется 194 памяти.
# Для 3 решения требуется 226 памяти.
# Для 4 решения требуется 180 памяти.
# Если по времени 1 и 4 вариант были самые оптимальные, то по памяти 2 и 4 вариант сильно лучше.
