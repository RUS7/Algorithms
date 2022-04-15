# 3 вариант

import sys
import random


def revers(i_min, i_max):
    array[i_min], array[i_max] = array[i_max], array[i_min]


SIZE_N = 20
MIN_ITEM = 0
MAX_ITEM = 1000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
print(array, '\n')

array_sort = sorted(array)
min_ = array_sort[0]
max_ = array_sort[len(array_sort) - 1]
i_min = array.index(min_)
i_max = array.index(max_)

revers(i_min, i_max)
print(array)

print('*' * 100)
print(sys.getsizeof(array))                       #256
print(sys.getsizeof(array_sort))                  #280
print(sys.getsizeof(min_))                        #28
print(sys.getsizeof(max_))                        #28
print(sys.getsizeof(i_min))                       #28
print(sys.getsizeof(i_max))                       #28
print(sys.getsizeof(revers(i_min, i_max)))        #16

                                                  #664
