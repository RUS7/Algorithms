#  Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
#  Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.


from hashlib import sha1


def count_sub(data):
    result = set()
    for i in range(len(data)):
        for j in range(i + 1, len(data) + 1):
            if sha1(line[i:j].encode('utf-8')).hexdigest() != sha1(line.encode('utf-8')).hexdigest():
                result.add(sha1(line[i:j].encode('utf-8')).hexdigest())
    return len(result)


line = input("Введите строку: ")
print(count_sub(line))
