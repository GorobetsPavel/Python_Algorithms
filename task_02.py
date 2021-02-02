# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
import timeit
import cProfile

def infinity():
    idx = 0
    while 1:
        yield idx
        idx += 1


def sieve(idx=10_000, n=150_000):
    _sieve = [i for i in range(n)]

    _sieve[1] = 0
    sn = 0

    i = 2
    while i <= n-1:
        if _sieve[i] != 0:
            sn += 1
            if sn == idx:
                return _sieve[i]
            j = i + i
            while j < n:
                _sieve[j] = 0
                j += i
        i += 1
    print('Введено слишком большое число.')


def prime_slow(idx=10_000):
    new_list = []
    for i in infinity():
        if i > 2:
            for j in new_list:
                if i % j == 0:
                    break
            else:
                new_list.append(i)
                if len(new_list) == idx:
                    return new_list[idx - 1]


def prime(idx=10_000):
    assert idx >= 1, 'Число должно быть больше 0'
    if idx == 1:
        return 2
    sn = 1
    for i in infinity():
        if i >= 3 and i % 2 != 0:
            j = 3
            while j * j <= i and i % j != 0:
                j += 2
            if j * j > i:
                sn += 1
                if idx == sn:
                    return i


# ind = int(input('Ввести натуральное число: '))
# num = sieve(ind)
# print(sieve(1_000_000))
# print(prime(10_000))
# print(sieve(10))

# print(prime_v_02(1_000_000)) # 15485863

# for i in range(1, 500):
#     print(prime(i), sieve(i))
# print(sieve())
# print(prime_slow())
# print(prime())

# print(timeit.timeit('sieve(10)', number=100, globals=globals()))        # 2.9937496
# print(timeit.timeit('sieve(100)', number=100, globals=globals()))       # 3.5858779000000003
# print(timeit.timeit('sieve(1000)', number=100, globals=globals()))      # 4.432454099999999
# print(timeit.timeit('sieve(10000)', number=100, globals=globals()))     # 6.931964399999998

# print(timeit.timeit('sieve(10, 150)', number=100, globals=globals()))          # 0.0025833999999999996
# print(timeit.timeit('sieve(100, 1_500)', number=100, globals=globals()))       # 0.0522769
# print(timeit.timeit('sieve(1000, 15_000)', number=100, globals=globals()))     # 0.49078560000000004
# print(timeit.timeit('sieve(10000, 150_000)', number=100, globals=globals()))   # 6.3849964
# print(timeit.timeit('sieve(40000, 600_000)', number=100, globals=globals()))   # 9.510318999999999

# print(timeit.timeit('prime_slow(10)', number=100, globals=globals()))     # 0.0025050999999999962
# print(timeit.timeit('prime_slow(100)', number=100, globals=globals()))    # 0.1000343
# print(timeit.timeit('prime_slow(1000)', number=100, globals=globals()))   # 4.0069002
# print(timeit.timeit('prime_slow(10000)', number=100, globals=globals()))  # 1248.2033799999999

# print(timeit.timeit('prime(10)', number=100, globals=globals()))          # 0.0074144999999999905
# print(timeit.timeit('prime(100)', number=100, globals=globals()))         # 0.07169790000000001
# print(timeit.timeit('prime(1000)', number=100, globals=globals()))        # 0.6219277
# print(timeit.timeit('prime(10000)', number=100, globals=globals()))       # 25.3243617


# cProfile.run('sieve()')
#      5 function calls in 0.112 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.001    0.001    0.112    0.112 <string>:1(<module>)
#     1    0.095    0.095    0.111    0.111 task_02.py:17(sieve)
#     1    0.016    0.016    0.016    0.016 task_02.py:18(<listcomp>)
#     1    0.000    0.000    0.112    0.112 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('prime()')
#      104735 function calls in 0.274 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.274    0.274 <string>:1(<module>)
# 104731    0.015    0.000    0.015    0.000 task_02.py:10(infinity)
#     1    0.259    0.259    0.274    0.274 task_02.py:50(prime)
#     1    0.000    0.000    0.274    0.274 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# print(timeit.timeit('prime(1_000_000)', number=1, globals=globals()))                  #354.5937901.
# print(timeit.timeit('sieve(1_000_000, 16_000_000)', number=1, globals=globals()))      #13.6203176

# Через решето выполняется быстрее, меньше вызовов, но там приходится кроме самого числа еще двигать максимальный размер
# массива. Хочется туда как то прикрутить бесконечный массив, но в этой реализации не сообразил как сделать.
# простое число под номером 1_000_000 удалось найти за 13.6203176, Но пришлось увеличить размер массива до 16_000_000
# Функция prime очень сильно замедляется, с увеличением запрашиваемого числа.
# Сначала сделал функцию prime_slow. Попробовал сделать проверку делится ли число на те числа, которые являются простыми
# но там со скоростью вообще беда получается. До 1_000 числа еще вменяемые результаты (в 4 раза замедляется поиск), то
# после там уже очень медленно.
