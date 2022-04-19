"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


# Делю массив на части
def merge_sort(data):
    n = len(data)
    if n <= 1:
        return data
    else:
        middle = len(data) // 2               # нахожу середину массива
        left = merge_sort(data[:middle])      # включаю то, что слева середины масива
        right = merge_sort(data[middle:])     # включаю то, что справа середины масива
        return merge(left, right)



# Сортирую
def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]
    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right
    return res



SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50


# Рандомно создаю массив вещественных числел(с окр. до 3 знаков после запятой)
array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 3) for _ in range(SIZE)]
print('Исходный массив:\n', array)
array_sort = merge_sort(array)
print('Отсотированный по возростанию массив: \n', array_sort)






