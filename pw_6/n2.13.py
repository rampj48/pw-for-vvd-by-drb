numbers = [2, 5, 3, 6, 98, 1, 9, 0]
result = []

for number in numbers:
    if number < 15:
        result.append(number * 2)
    else:
        result.append(number)

print(result)
