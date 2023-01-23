import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if not b or a[i] != b[-1]:
            b.append(a[i])
    n = len(b)
    cnt = 0
    #print(b)
    #print(a)
    for i in range(n):
        prev = True
        nxt = True
        if i > 0:
            if b[i-1] <= b[i]:
                prev = False
        if i < n-1:
            if b[i] >= b[i+1]:
                nxt = False
        if prev and nxt: cnt += 1
    if cnt == 1:
        print('YES')
    else:
        print('NO')
