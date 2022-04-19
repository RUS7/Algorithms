
# 2 вариант

import sys
import random

SIZE_N = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
print(array, '\n')

i_max = array.index(max(array))
i_min = array.index(min(array))

array[i_min], array[i_max] = array[i_max], array[i_min]

print(array)

print('*' * 100)
print(sys.getsizeof(array))
print(sys.getsizeof(i_max))
print(sys.getsizeof(i_min))

sum_ = sys.getsizeof(array) + sys.getsizeof(i_min) + sys.getsizeof(i_max)
print(f'Общая сумма занимаемой памяти {sum_} байт')