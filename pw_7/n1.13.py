def check_armstrong(number):
    suma = []
    for digit in str(number):
        suma.append(int(digit) ** int(len(str(number))))
    if number == sum(suma):
        return True


k = int(input())
for i in range(1, k):
    if check_armstrong(i):
        print(i)
