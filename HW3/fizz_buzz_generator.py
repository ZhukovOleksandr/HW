import random

# values initialization
print('Введите начальное стартовое значение:')
start_value = int(input())

print('Введите конечное стартовое значение:')
stop_value = int(input())

# creating file with number sequence
print('Ведите назвение будущего файла:')
file_name = str(input())

# creating a number sequence
range_list = []

for numb in range(20):
    fizz = random.randint(start_value, stop_value)
    range_list.append(str(fizz))
    buzz = random.randint(start_value + fizz, stop_value + fizz)
    range_list.append(str(buzz))
    stop_numb = random.randint(start_value + buzz, stop_value + buzz)
    range_list.append(str(stop_numb))

    range_list_str = ' '.join(range_list)

    with open('%s' % file_name + '.txt', 'a') as range_file:
        range_file.write(range_list_str + '\n')
        range_file.close()

    range_list.clear()
