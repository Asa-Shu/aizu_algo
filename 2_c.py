import copy


def bubbleSort(A, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if int(A[j - 1][1]) > int(A[j][1]):
                A[j - 1], A[j] = A[j], A[j - 1]
    return A


def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        A[i], A[minj] = A[minj], A[i]
        i += 1
    return A


N = int(input())
A = input().split()
A_ = copy.copy(A)
# *A_, = A も可 寧ろこっちのがいいと思う。

b = bubbleSort(A, N)
print(*b)
print('Stable')
s = selectionSort(A_, N)
print(*s)
print('Stable' if b == s else 'Not stable')
