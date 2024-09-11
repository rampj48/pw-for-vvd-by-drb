def check(number):
    if (str(number)[0]) == (str(number)[-1]):
        return True
    else:
        return False


x = int(input())
print(check(x))
