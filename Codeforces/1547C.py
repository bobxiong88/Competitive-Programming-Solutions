import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    k, n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = a[::-1]
    b = b[::-1]
    ans = []
    pos = True
    while a or b:
        init = (len(a), len(b))
        while a and a[-1] == 0:
            k += 1
            ans.append(a.pop())
        while b and b[-1] == 0:
            k += 1
            ans.append(b.pop())
        while a and a[-1] <= k and a[-1]:
            ans.append(a.pop())
        while b and b[-1] <= k and b[-1]:
            ans.append(b.pop())
        fin = (len(a), len(b))
        if a+b and fin==init:
            pos = False
            break
    if not pos:
        print(-1)
    else:
        print(*ans)
