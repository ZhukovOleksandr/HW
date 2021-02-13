# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!

def sub_str(string1):
    return string1.lower()


with open('Thomas Dylan.txt', 'r') as poetry:
    poetry_list = poetry.read().split()

poetry_list1 = list(map(sub_str, poetry_list))
poerty_count = set(list(map(lambda n: '\n' + n + ':' + ' ' + str(poetry_list1.count(n)), poetry_list1)))

print(*poerty_count)
