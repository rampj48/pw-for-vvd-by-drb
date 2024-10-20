a = int(input("Введите число a - "))
b = int(input("Введите число b - "))

for number in range(a, b - 1, -1):
    if number % 2 != 0:
        print(number)
