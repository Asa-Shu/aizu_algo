# 挿入ソート
N = int(input())
A = list(map(int, input().split()))

def insertionSort(N, A):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:  # vより大きい要素は後ろにずらす
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print(*A)


print(*A)
insertionSort(N, A)
