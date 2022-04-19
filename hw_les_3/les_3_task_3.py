
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE_N = 10
MIN_ITEM = max_it = 0
MAX_ITEM, min_it = 100, 100
i_min = 0
i_max = 0

a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
print(a, '\n')
for i in range(len(a)):
    if a[i] < min_it:
        min_it = a[i]
        i_min = i
    if a[i] > max_it:
        max_it = a[i]
        i_max = i

print(f'Минимальное число: %d, максимальное число: %d' % (min_it, max_it))
print()
a[i_min], a[i_max] = a[i_max], a[i_min]
print(a)
