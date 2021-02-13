# Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку,
# берете из нее числа, считаете для них fizzbuzz, выводите.
# Переделать вторую задачу так, чтобы результат писался в другой файл.


sequence = open('FB_number_list.txt', 'r')
result = []

print('Ведите назвение будущего файла:')
file_name = str(input())


for elem in sequence:
    numb_list = list(map(int, elem.split()))
    fizz, buzz, stop_numb = numb_list

    for i in range(1, stop_numb + 1, 1):
        if i % fizz == 0 and i % buzz == 0:
            i = 'FB'
            result.append(str(i))
        elif i % fizz == 0:
            i = 'F'
            result.append(str(i))
        elif i % buzz == 0:
            i = 'B'
            result.append(str(i))
        else:
            result.append(str(i))

    print(*result)

    result_str = ' '.join(result)
    with open('%s' % file_name + '.txt', 'a') as new_file:
        new_file.write(result_str + '\n')
        new_file.close()

    result.clear()
