# 4.Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 8
MIN_ITEIM = 0
a = [random.randint(MIN_ITEIM, SIZE) for _ in range(SIZE + 2)]
print(a)
num = a[0]
quantity_max = 1
for i in range(len(a)):
    quantity = 1
    for j in range((i + 1), len(a)):
        if a[i] == a[j]:
            quantity += 1
    if quantity > quantity_max:
        quantity_max = quantity
        num = a[i]

print(quantity_max, 'раз(а) встречается число', num)
