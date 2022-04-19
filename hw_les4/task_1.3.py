# вариант 3
import random
import timeit
import cProfile


def min_min(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)
    return min_1, min_2

print(timeit.timeit('min_min(10)', globals=globals(), number=1000))       # 0.04847707800000001
print(timeit.timeit('min_min(100)', globals=globals(), number=1000))      # 0.297899897
print(timeit.timeit('min_min(1000)', globals=globals(), number=1000))     # 2.686708326
print(timeit.timeit('min_min(10000)', globals=globals(), number=1000))    # 27.894595431
print(timeit.timeit('min_min(100000)', globals=globals(), number=1000))   # 270.634697551

# Линейная сложность алгоритма

cProfile.run('min_min(10000)')

"""
 53090 function calls in 0.040 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.040    0.040 <string>:1(<module>)
    10000    0.013    0.000    0.025    0.000 random.py:200(randrange)
    10000    0.007    0.000    0.032    0.000 random.py:244(randint)
    10000    0.009    0.000    0.012    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.040    0.040 task_1.3.py:7(min_min)
        1    0.008    0.008    0.039    0.039 task_1.3.py:8(<listcomp>)
        1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
        2    0.001    0.000    0.001    0.000 {built-in method builtins.min}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13082    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
"""