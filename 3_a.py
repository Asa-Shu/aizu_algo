# pythonのlistには元々pop()とappend()（pushの代わり）がある。

stack = []
for ele in input().split():
    if ele in '+-*':
        v2 = stack.pop()
        v1 = stack.pop()
        stack.append(str(eval(v1 + ele + v2)))  # eval関数は第1引数を式として評価。例えば、eval(‘2 + 3’)とすると5を返す。
    else:
        stack.append(ele)

print(*stack)
