a = int(input())
b = int(input())
if a < b:
    x = 2 * a + 2 * b
elif a > b:
    x = a - b + 1
else:
    x = b ** 2 - b
print(x)
