n = int(input())
*A, = map(int, input().split())


def selectionSort(A, n):
    c = 0
    for i in range(n):
        minj = i

        for j in range(i + 1, n):
            if A[minj] > A[j]:
                minj = j
        A[i], A[minj] = A[minj], A[i]
        if A[i] != A[minj]:  # 同じ数値で入れ替えた時はカウントしない
            c += 1
    return (A, c)


A, c = selectionSort(A, n)
print(*A)
print(c)
