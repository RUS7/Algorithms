
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for i in range(2, 10):
    n = 0
    for j in range(2, 101):
        if j % i == 0:
            n += 1

    print(f'На число {i} делится {n} чисел(числа)')