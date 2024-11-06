def check_prime(num, div=2):
    if num <= 1:
        return "NO"
    if num == div:
        return "YES"
    if num % div == 0:
        return "NO"

    return check_prime(num, div + 1)


n = int(input("Введите натуральное число большее 1: "))
print(check_prime(n))
