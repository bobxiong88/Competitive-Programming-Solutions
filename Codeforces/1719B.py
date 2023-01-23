import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    k = k%4
    res = []
    if n%4 == 0:
        for i in range(1,n+1,4):
            if k%2:
                res.append((i,i+1))
                res.append((i+2, i+3))
            elif k==2:
                res.append((i+1,i))
                res.append((i+2,i+3))
    else:
        if k%2:
            for i in range(1,n-1,4):
                res.append((i,i+1))
                res.append((i+2, i+3))
            res.append((n-1,n))
        elif k==2:
            for i in range(1,n-1,4):
                res.append((i+1,i))
                res.append((i+2,i+3))
            res.append((n, n-1))
    if res:
        print("YES")
    else:
        print("NO")
    for i in res:
        print(*i)
            
