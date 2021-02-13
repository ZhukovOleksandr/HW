# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map


print("Какое колличество простых чисел Вам необходимо?")
numb_quantity = int(input())

print("Введите стартовое значение (число), от которого следует начать отсчет:")
simple_numb = int(input())

numbers_list = []

while len(numbers_list) < numb_quantity:
    divisor_list = []
    for i in range(1, simple_numb + 1, 1):
        if simple_numb % i == 0:
            divisor_list.append(i)

    if len(divisor_list) == 2:
        numbers_list.append(simple_numb)
    simple_numb += 1
    divisor_list.clear()
str_numb_list = ' '.join(map(str, numbers_list))
with open("simple_number.txt", 'w') as new_file:
    new_file.write(str_numb_list)
