# 2). Написать два алгоритма нахождения i-го по счёту
# простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.


# Второй — без использования «Решета Эратосфена».


import timeit
import cProfile

def prime_number(num_account):
    count = 1
    current_prime = 2

    while count < num_account:
        current_prime += 1
        for i in range(2, current_prime):
            if current_prime % i == 0:
                break
        else:

            count += 1

    return current_prime



#print(timeit.timeit('prime_number(10)', globals=globals(), number=1000))         # 0.033945736
#print(timeit.timeit('prime_number(100)', globals=globals(), number=1000))        # 2.96565935
#print(timeit.timeit('prime_number(1000)', globals=globals(), number=1000))       # 496.09996773399996
print(timeit.timeit('prime_number(10000)', globals=globals(), number=1000))       #



cProfile.run('prime_number(10000)')

"""
         4 function calls in 0.556 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.556    0.556 <string>:1(<module>)
        1    0.556    0.556    0.556    0.556 task_2.1.py:14(prime_number)
        1    0.000    0.000    0.556    0.556 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0


"""