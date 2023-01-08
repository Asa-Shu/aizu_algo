cnt = 0


def insertionSort(A, n, g):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            global cnt
            cnt += 1
        A[j + g] = v
    return A


def shellSort(A, n):
    lst = []
    i = 0
    while 3 * i + 1 <= n:
        lst.append(3 * i + 1)
        i = 3 * i + 1
    G = lst[::-1]
    m = len(G)
    for i in range(m):
        insertionSort(A, n, G[i])
    return A, m, G


n = int(input())
A = [int(input()) for i in range(n)]

A, m, G = shellSort(A, n)

print(m)
print(*G)
print(cnt)
print(*A, sep='\n')

# 複数行のリスト読み込みは、A = list(map(int, sys.stdin)) もあり。
