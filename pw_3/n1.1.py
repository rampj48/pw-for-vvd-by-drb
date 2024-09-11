def check(number):
    if number in range(1, 4):
        return True
    else:
        return False


x = int(input())
y = int(input())
z = int(input())

print(check(x), check(y), check(z))
