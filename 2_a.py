n = int(input())
*A, = map(int, input().split())


def bubbleSort(A, n):
    flag = 1
    i = 0  # 未ソート部分の先頭インデックス
    swapCount = 0
    while flag:
        flag = 0
        for j in reversed(range(i + 1, n)):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                swapCount += 1
                flag = 1
        i += 1

    return (A, swapCount)


A, swapCount = bubbleSort(A, n)
print(*A)
print(swapCount)
