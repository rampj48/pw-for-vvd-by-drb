number = input()
even = []
odd = []

for i in number:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print('Четные цифры - ', ', '.join(even))
print('Нечетные цифры - ', ', '.join(odd))
