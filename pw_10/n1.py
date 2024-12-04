import numpy as np

matrix = open("БДР_УБ-42_vvod.txt").read()
matrix = np.array([item.split() for item in matrix.split("\n")[:-1]])
rows, columns = matrix.shape

file = open("БДР_УБ-42_vivod.txt", "w")
file.write("Результат задания №1:\n")
file.write("Наименьшие элементы каждой четной строки:")

for i in range(1, rows + 1, 2):
    file.write(" ")
    try:
        file.write(min(matrix[i]))
    except IndexError:
        pass

file.write("\n" * 2)
file.close()
