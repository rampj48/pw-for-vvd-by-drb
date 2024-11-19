import random

M = int(input())
N = int(input())
A = [[random.randrange(10) for i in range(M)] for j in range(N)]

for i in A:
    print(' '.join(list(map(str, i))))

for i in range(1, N + 1, 2):
    try:
        print(min(A[i]))
    except IndexError:
        pass
