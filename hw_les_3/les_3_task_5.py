
'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
'''

import random

SIZE = 10
MIN_ITEIM = -10
array = [random.randint(MIN_ITEIM, SIZE) for _ in range(SIZE)]
print(array, '\n')

max_negative_iteim = MIN_ITEIM - 1
num = 0

for i in range(len(array)):
    if max_negative_iteim < array[i] < 0:
        max_negative_iteim = array[i]
        num = i

print(('Максимальный отрицательный элемент: %d, его индекс в массиве: %d' % (
max_negative_iteim, num)) if MIN_ITEIM <= max_negative_iteim < 0 else 'В массиве нет отрицательных элементов.')
