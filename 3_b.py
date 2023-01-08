# リストで実装
n, q = map(int, input().split())

queue = []
for i in range(n):
    lst = input().split()
    lst[1] = int(lst[1])
    queue.append(lst)

t = 0
while True:
    if len(queue) == 0:
        break
    if queue[0][1] > q:  # 消滅しない場合
        queue[0][1] -= q
        t += q
        queue.append(queue.pop(0))  # 先頭から消して末尾に追加
    else:  # 消滅する場合
        t += queue[0][1]
        print(queue[0][0] + ' ' + str(t))
        queue.pop(0)
