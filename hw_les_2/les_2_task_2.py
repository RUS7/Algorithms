'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''


def func(A, even = 0, odd = 0):
    if A <= 0:
        return even, odd
    else:
        cur_A = A % 10
        A = A // 10
        if cur_A % 2 == 0:
            even += 1
        else:
            odd += 1
        return func(A, even, odd)


A = int(input("Введите натуральное число A: "))
even, odd = func(A)
print(f"Четных: %d, Нечетных: %d" %(even, odd))

