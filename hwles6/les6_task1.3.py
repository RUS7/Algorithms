# 3 вариант

import sys
import random



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
array[i_min], array[i_max] = array[i_max], array[i_min]

print(array)

print('*' * 100)
print(sys.getsizeof(array))
print(sys.getsizeof(array_sort))
print(sys.getsizeof(min_))
print(sys.getsizeof(max_))
print(sys.getsizeof(i_min))
print(sys.getsizeof(i_max))
sum_ = sys.getsizeof(array) + sys.getsizeof(array_sort) + sys.getsizeof(min_) + sys.getsizeof(max_) +sys.getsizeof(i_min) + sys.getsizeof(i_max)
print(f'Общая сумма занимаемой памяти {sum_} байт')
