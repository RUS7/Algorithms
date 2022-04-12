# 2 вариант
import random
import timeit
import cProfile


def min_while(size):
    array = [random.randint(size * - 10, size * 10) for _ in range(size)]
    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)
    i = 2
    while i < len(array):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i
        i += 1
    return array[min_first], array[min_second]


print(timeit.timeit('min_while(10)', globals=globals(), number=1000))        # 0.030708431
print(timeit.timeit('min_while(100)', globals=globals(), number=1000))       # 0.352145505
print(timeit.timeit('min_while(1000)', globals=globals(), number=1000))      # 4.097528876
print(timeit.timeit('min_while(10000)', globals=globals(), number=1000))     # 38.899253933
print(timeit.timeit('min_while(100000)', globals=globals(), number=1000))    # 340.537432635

# Линейная сложность алгоритма

cProfile.run('min_while(1000)')

"""
6675 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
     1000    0.001    0.000    0.003    0.000 random.py:200(randrange)
     1000    0.001    0.000    0.003    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.001    0.001    0.005    0.005 task_1.2.py:7(min_while)
        1    0.001    0.001    0.004    0.004 task_1.2.py:8(<listcomp>)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
      999    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1671    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# Наиболее быстрый вариант