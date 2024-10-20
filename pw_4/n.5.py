n = int(input("Введите число n - "))
suma = 0
for number in range(1, n + 1):
    suma += number ** 3
print("Сумма =", suma)
