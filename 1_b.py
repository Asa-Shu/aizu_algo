# ユークリッドの互除法  O(log b)
x, y = map(int, input().split())


def gcd(x, y):
    if x < y:
        x, y = y, x

    while y > 0:
        r = x % y
        x = y
        y = r
    return x


print(gcd(x, y))

# 別解
x, y = map(int, input().split())


def gcd(x, y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x


print(gcd(x, y))
