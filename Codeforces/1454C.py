import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    curr = a[0]
    for i in range(n):
        if a[i] != curr:
            b.append(curr)
            curr = a[i]
    b.append(curr)
    pos = [[] for i in range(n+1)]
    ans = float('inf')
    for i in range(len(b)):
        pos[b[i]].append(i)
    for i in pos:
        if not i: continue
        curr = len(i)+1
        if i[0] == 0:
            curr-=1
        if i[-1] == len(b)-1:
            curr-=1
        ans = min(curr,ans)
    print(ans)
