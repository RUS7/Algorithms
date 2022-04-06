
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE_N = 10
MIN_ITEM = max_it = 0
MAX_ITEM, min_it = 100, 100
i_min = 0
i_max = 0

summ_slice = 0

a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
print(a, '\n')
for i in range(len(a)):
    if a[i] < min_it:
        min_it = a[i]
        i_min = i
    if a[i] > max_it:
        max_it = a[i]
        i_max = i

print(f'Минимальное число: %d, максимальное число: %d '%(min_it, max_it))
print()

if i_min < i_max:
    print('Cумма элементов, находящихся между минимальным и максимальным элементами равна ', sum(a[(i_min+1):i_max]))
else:
    print('Cумма элементов, находящихся между минимальным и максимальным элементами равна ', sum(a[(i_max+1):i_min]))

