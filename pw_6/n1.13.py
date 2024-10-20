numbers = [2, 78, 435, 2, 74, 23, 455, 2, 78, 34]
indexes = dict()

for index, number in enumerate(numbers):
    if number in indexes:
        indexes[number].append(index)
    else:
        indexes[number] = [index]

for number, index in indexes.items():
    if len(index) > 1:
        print(number, index)
