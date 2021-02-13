def numb_sq(numb):
    return numb ** 2


print("Веедите название файла, который необходимо прочесть:")

file_name = str(input())

with open('%s' % file_name + '.txt', 'r') as simp_number:
    simple_list = list(map(int, (simp_number.readline().split())))

numb_sq_list = list(map(numb_sq, simple_list))
print(numb_sq_list)
