# 2 вариант

import sys
import random

SIZE_N = 20
MIN_ITEM = 0
MAX_ITEM = 1000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
print(array, '\n')

i_max = array.index(max(array))
i_min = array.index(min(array))

def revers(i_min, i_max):
    array[i_min], array[i_max] = array[i_max], array[i_min]

revers(i_min, i_max)
print(array)


print('*' * 100)
print(sys.getsizeof(array))                   #256
print(sys.getsizeof(i_max))                   #28
print(sys.getsizeof(i_min))                   #28
print(sys.getsizeof(revers(i_min, i_max)))    #16

                                              #328