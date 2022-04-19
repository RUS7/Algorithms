'''
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''


def func(n, A =1, amount=1):
    if n > 0:
        A /= (-2)
        n -= 1
        amount += A
        return func(n, A, amount)
    else:
        return amount


n = int(input("Введите натуральное число n: "))
if n == 0:
    amount = 0
else:
    amount = func(n - 1)
print(f"сумма элементов: {amount}")
