# Взял задачу из 3 практического задания №3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import timeit
import cProfile

array_min_num = 0
array_max_num = 1000


def find_min(_array, min_num, i, array_len):
    if _array[i] < min_num:
        min_num = _array[i]
    if i == array_len:
        return min_num
    else:
        return find_min(_array, min_num, i + 1, array_len)


def find_max(_array, max_num, i, array_len):
    if _array[i] > max_num:
        max_num = _array[i]
    if i == array_len:
        return max_num
    else:
        return find_max(_array, max_num, i + 1, array_len)


def find_min_max_id(_array, max_num, min_num, i, array_len, max_id, min_id):
    if _array[i] > max_num:
        max_num = _array[i]
        max_id = i
    if _array[i] < min_num:
        min_num = _array[i]
        min_id = i
    if i == array_len:
        return min_id, max_id
    else:
        return find_min_max_id(_array, max_num, min_num, i + 1, array_len, max_id, min_id)


def main_v_01(array_size):
    random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
    # print(random_array)
    max_id = 0
    min_id = 0
    min_num = random_array[0]
    max_num = min_num

    for i, elem in enumerate(random_array):
        if elem > max_num:
            max_id = i
            max_num = elem
        if elem < min_num:
            min_id = i
            min_num = elem

    random_array[max_id], random_array[min_id] = random_array[min_id], random_array[max_id]
    # print(random_array)


def main_v_02_without_num(array_size):
    random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
    # print(random_array)
    max_id = 0
    min_id = 0

    for i in range(array_size):
        if random_array[i] > random_array[max_id]:
            max_id = i
        if random_array[i] < random_array[min_id]:
            min_id = i

    random_array[max_id], random_array[min_id] = random_array[min_id], random_array[max_id]
    # print(random_array)


def main_v_03_recursion(array_size):
    random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
    # print(random_array)

    id_min_max = find_min_max_id(random_array, random_array[0], random_array[0], 1, len(random_array) - 1, 0, 0)
    min_id = id_min_max[0]
    max_id = id_min_max[1]

    random_array[max_id], random_array[min_id] = random_array[min_id], random_array[max_id]
    # print(random_array)


def main_v_04_with_func(array_size):
    random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
    # print(random_array)

    min_num = find_min(random_array, random_array[0], 1, array_size - 1)
    max_num = find_max(random_array, random_array[0], 1, array_size - 1)
    max_id = random_array.index(max_num)
    min_id = random_array.index(min_num)
    random_array[max_id], random_array[min_id] = random_array[min_id], random_array[max_id]
    # print(random_array)


def main_v_05(array_size):
    random_array = [random.randint(array_min_num, array_max_num) for i in range(array_size)]
    # print(random_array)

    min_num = min(random_array)
    max_num = max(random_array)
    max_id = random_array.index(max_num)
    min_id = random_array.index(min_num)
    random_array[max_id], random_array[min_id] = random_array[min_id], random_array[max_id]
    # print(random_array)


# main_v_01(20)
# main_v_02_without_num(20)
# main_v_03_recursion(20)
# main_v_04_with_func(20)
# main_v_05(20)

#
# print(timeit.timeit('main_v_01(100)', number=1000, globals=globals()))                # 0.09997139999999999
# print(timeit.timeit('main_v_01(200)', number=1000, globals=globals()))                # 0.1912411
# print(timeit.timeit('main_v_01(400)', number=1000, globals=globals()))                # 0.3861701
# print(timeit.timeit('main_v_01(800)', number=1000, globals=globals()))                # 0.7695505

# print(timeit.timeit('main_v_02_without_num(100)', number=1000, globals=globals()))     # 0.10886990000000002
# print(timeit.timeit('main_v_02_without_num(200)', number=1000, globals=globals()))     # 0.20611510000000002
# print(timeit.timeit('main_v_02_without_num(400)', number=1000, globals=globals()))     # 0.4135515
# print(timeit.timeit('main_v_02_without_num(800)', number=1000, globals=globals()))     # 0.8415060999999999

# print(timeit.timeit('main_v_03_recursion(100)', number=1000, globals=globals()))      # 0.11181929999999998
# print(timeit.timeit('main_v_03_recursion(200)', number=1000, globals=globals()))      # 0.22083900000000004
# print(timeit.timeit('main_v_03_recursion(400)', number=1000, globals=globals()))      # 0.4517463
# print(timeit.timeit('main_v_03_recursion(800)', number=1000, globals=globals()))      # 1.0750818
#
# print(timeit.timeit('main_v_04_with_func(100)', number=1000, globals=globals()))      # 0.127285
# print(timeit.timeit('main_v_04_with_func(200)', number=1000, globals=globals()))      # 0.2433693
# print(timeit.timeit('main_v_04_with_func(400)', number=1000, globals=globals()))      # 0.506826
# print(timeit.timeit('main_v_04_with_func(800)', number=1000, globals=globals()))      # 1.0269872000000002
#
# print(timeit.timeit('main_v_05(100)', number=1000, globals=globals()))                # 0.0977876
# print(timeit.timeit('main_v_05(200)', number=1000, globals=globals()))                # 0.1840472
# print(timeit.timeit('main_v_05(400)', number=1000, globals=globals()))                # 0.3872599
# print(timeit.timeit('main_v_05(800)', number=1000, globals=globals()))                # 0.7405344999999999

# cProfile.run('main_v_01(200)')
#      1013 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#   200    0.000    0.000    0.000    0.000 random.py:200(randrange)
#   200    0.000    0.000    0.000    0.000 random.py:244(randint)
#   200    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 task_01.py:42(main_v_01)
#     1    0.000    0.000    0.000    0.000 task_01.py:43(<listcomp>)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#   200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   208    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main_v_01(400)')
#      2013 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#   400    0.000    0.000    0.001    0.000 random.py:200(randrange)
#   400    0.000    0.000    0.001    0.000 random.py:244(randint)
#   400    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.001    0.001 task_01.py:42(main_v_01)
#     1    0.000    0.000    0.001    0.001 task_01.py:43(<listcomp>)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#   400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   408    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('main_v_01(800)')

#      4028 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#   800    0.001    0.000    0.001    0.000 random.py:200(randrange)
#   800    0.000    0.000    0.002    0.000 random.py:244(randint)
#   800    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.002    0.002 task_01.py:42(main_v_01)
#     1    0.000    0.000    0.002    0.002 task_01.py:43(<listcomp>)
#     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#   800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   823    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main_v_05(200)')
#
#      1011 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#   200    0.000    0.000    0.000    0.000 random.py:200(randrange)
#   200    0.000    0.000    0.000    0.000 random.py:244(randint)
#   200    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 task_01.py:102(main_v_05)
#     1    0.000    0.000    0.000    0.000 task_01.py:103(<listcomp>)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#   200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   202    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('main_v_05(400)')
#
#      2021 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#   400    0.000    0.000    0.001    0.000 random.py:200(randrange)
#   400    0.000    0.000    0.001    0.000 random.py:244(randint)
#   400    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.001    0.001 task_01.py:102(main_v_05)
#     1    0.000    0.000    0.001    0.001 task_01.py:103(<listcomp>)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#   400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   412    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('main_v_05(800)')
#
#      4031 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#   800    0.001    0.000    0.001    0.000 random.py:200(randrange)
#   800    0.000    0.000    0.001    0.000 random.py:244(randint)
#   800    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.002    0.002 task_01.py:102(main_v_05)
#     1    0.000    0.000    0.002    0.002 task_01.py:103(<listcomp>)
#     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#   800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   822    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('main_v_03_recursion(200)')

#  1209 function calls (1011 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    200    0.000    0.000    0.000    0.000 random.py:200(randrange)
#    200    0.000    0.000    0.000    0.000 random.py:244(randint)
#    200    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#  199/1    0.000    0.000    0.000    0.000 task_01.py:29(find_min_max_id)
#      1    0.000    0.000    0.001    0.001 task_01.py:78(main_v_03_recursion)
#      1    0.000    0.000    0.000    0.000 task_01.py:79(<listcomp>)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    204    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main_v_03_recursion(400)')

#      2412 function calls (2014 primitive calls) in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#   400    0.000    0.000    0.001    0.000 random.py:200(randrange)
#   400    0.000    0.000    0.001    0.000 random.py:244(randint)
#   400    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
# 399/1    0.000    0.000    0.000    0.000 task_01.py:29(find_min_max_id)
#     1    0.000    0.000    0.002    0.002 task_01.py:78(main_v_03_recursion)
#     1    0.000    0.000    0.001    0.001 task_01.py:79(<listcomp>)
#     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   407    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('main_v_03_recursion(800)')
#      4826 function calls (4028 primitive calls) in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   800    0.001    0.000    0.001    0.000 random.py:200(randrange)
#   800    0.000    0.000    0.002    0.000 random.py:244(randint)
#   800    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
# 799/1    0.001    0.000    0.001    0.001 task_01.py:29(find_min_max_id)
#     1    0.000    0.000    0.003    0.003 task_01.py:78(main_v_03_recursion)
#     1    0.000    0.000    0.002    0.002 task_01.py:79(<listcomp>)
#     1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   821    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Думал будет большая разница между проходом цикла и поиском с помощью функций минимального\максимального числа с
# последующей заменой. По факту разницы не особо много (зависимость линейная), все примеры увеличивают время ровно во столько раз, во сколько
# увеличивается массив. По времени оптимальные варианты 1 и 5 (то один быстрее, то второй). 3 вариант тоже близкий по
# скорости, но не будет работать при больших массивах (из-за рекурсии), да и вызовов там больше
