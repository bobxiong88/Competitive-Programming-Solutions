import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a[-1] == 0:
        print(*[i for i in range(1, n+2)])
        continue
    if a[0] == 1:
        print(n+1, *[i for i in range(1, n+1)])
        continue
    pos = []
    found = False
    for i in range(n-1):
        if a[i] == 0 and a[i+1] == 1:
            found = True
            res = [j for j in range(1, i+2)]
            res.append(n+1)
            for j in range(i+2, n+1):
                res.append(j)
            print(*res)
            found = True
            break
    if not found:
        print(-1)
