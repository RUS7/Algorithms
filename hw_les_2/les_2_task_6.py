'''
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
'''

import random
A = random.randint(0, 100)


def func(A, i = 10):
    i -= 1
    if i > 0:
        n = int(input('Введите число: '))
        if n == A:
            return print(f'Вы угадали. Загаданное число: {n}')
        elif n > A:
            print('Загаданное число меньше %d. У Вас осталось %d попыток.' % (n, i))
        else:
            print("Загаданное число больше %d. У Вас осталось %d попыток." % (n, i))
        return func(A, i)
    else:
        return print("Вы израходовали все свои попытки угадать число. Загаданное число: %d" % A)


print('Отгадайте число от 0 до 100. У Вас 10 попыток.')

res = func(A)


