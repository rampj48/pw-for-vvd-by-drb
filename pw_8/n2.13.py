import random

M = int(input())
N = int(input())
A = [[random.randrange(100) for i in range(M)] for j in range(N)]

for i in A:
    print(' '.join(list(map(str, i))))
print(" ")

max1 = max(map(max, A))
ind_max1 = A.index(max(A))
ind_max2 = A[ind_max1].index(max1)

min1 = min(map(min, A))
ind_min1 = A.index(min(A))
ind_min2 = A[ind_min1].index(min1)

A[ind_min1][ind_min2], A[ind_max1][ind_max2] = max1, min1

for i in A:
    print(*i)
