# 素数の数を数える
def isPrime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    i = 3
    while i <= x**(1 / 2):
        if x % i == 0:
            return False
        i += 2

    return True


n = int(input())
count = 0
for i in range(n):
    x = int(input())
    if isPrime(x):
        count += 1
print(count)
