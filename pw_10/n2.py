matrix = open("БДР_УБ-42_vvod.txt").read()
matrix = [item.split() for item in matrix.split("\n")[:-1]]

max1 = max(map(max, matrix))
ind_max1 = matrix.index(max(matrix))
ind_max2 = matrix[ind_max1].index(max1)

min1 = min(map(min, matrix))
ind_min1 = matrix.index(min(matrix))
ind_min2 = matrix[ind_min1].index(min1)

matrix[ind_min1][ind_min2], matrix[ind_max1][ind_max2] = max1, min1

file = open("БДР_УБ-42_vivod.txt", "a")
file.write("Результат задания №2:\n")
file.write("Изменённая матрица\n")

for i in matrix:
    for j in i:
        file.write(j)
        file.write(" ")
    file.write("\n")

file.close()
