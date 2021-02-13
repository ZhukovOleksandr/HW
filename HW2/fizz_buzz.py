print("Введите fizz:")
fizz = int(input())

print("Введите buzz:")
buzz = int(input())

print("Введите число, до которого необходимо досчитать:")
stop_numb = int(input())
result = []

for i in range(1, stop_numb + 1, 1):
    if i % fizz == 0 and i % buzz == 0:
        i = 'FB'
        result.append(i)
    elif i % fizz == 0:
        i = 'F'
        result.append(i)
    elif i % buzz == 0:
        i = 'B'
        result.append(i)

    else:
        result.append(i)
print(*result)
