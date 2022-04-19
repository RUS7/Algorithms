# Урок 3. Задача 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import timeit
import cProfile


# вариант 1
def min_for(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)

    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i
    return array[min_first], array[min_second]


print(timeit.timeit('min_for(10)', globals=globals(), number=1000))     # 0.038477391
print(timeit.timeit('min_for(100)', globals=globals(), number=1000))    # 0.32605657899999996
print(timeit.timeit('min_for(1000)', globals=globals(), number=1000))   # 2.9538726989999997
print(timeit.timeit('min_for(10000)', globals=globals(), number=1000))  # 32.761697981
print(timeit.timeit('min_for(100000)', globals=globals(), number=1000)) # 302.064652936

# Линейная сложность алгоритма

cProfile.run('min_for(10000)')

"""        
    53109 function calls in 0.044 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.043    0.043 <string>:1(<module>)
    10000    0.013    0.000    0.025    0.000 random.py:200(randrange)
    10000    0.007    0.000    0.032    0.000 random.py:244(randint)
    10000    0.009    0.000    0.012    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.008    0.008    0.039    0.039 task _1.1.py:10(<listcomp>)
        1    0.004    0.004    0.043    0.043 task _1.1.py:9(min_for)
        1    0.000    0.000    0.044    0.044 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13103    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
    """

