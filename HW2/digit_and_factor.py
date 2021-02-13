a = int(input())
my_list = []
decimal = 1
while a > 0:
    n = a % 10
    a = a//10
    my_list.append(str(n) + "*" + str(decimal))
    decimal *= 10
new_list = (list(reversed(my_list)))
print(*new_list, sep=' + ')
