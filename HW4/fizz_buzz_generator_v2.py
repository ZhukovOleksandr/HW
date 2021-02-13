import random

# creating file with number sequence
print('Ведите назвение будущего файла:')
file_name = str(input())

# values initialization

print('''Веддите необходимое количестов "троек" для файла Fizz_Buzz: ''')
count = int(input())

print('Введите начальное значение диапазона генерации чисел:')
start_value = int(input())

print('Введите конечное значение диапазона генерации чисел:')
stop_value = int(input())

for i in range(count):
    fizz = buzz = stop_numb = 0
    range_list = []

    while not fizz < buzz < stop_numb:
        fizz = str(random.randint(start_value, stop_value))
        buzz = str(random.randint(start_value, stop_value))
        stop_numb = str(random.randint(start_value, stop_value))

    range_list.append(fizz)
    range_list.append(buzz)
    range_list.append(stop_numb)

    print(range_list)

    range_list_str = ' '.join(range_list)

    with open('%s' % file_name + '.txt', 'a') as range_file:
        range_file.write(range_list_str + '\n')
        range_file.close()
