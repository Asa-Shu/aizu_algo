n = int(input())
minv = int(input())
maxv = -10**9

for i in range(1, n):
    nxt = int(input())
    maxv = max(maxv, nxt - minv)
    minv = min(minv, nxt)  # minvは最小値を更新して入れていく
print(maxv)
