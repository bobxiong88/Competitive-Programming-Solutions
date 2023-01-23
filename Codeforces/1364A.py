import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    p = []
    a = tuple(map(int,input().split()))
    s = 0
    c = 0
    for i in range(n):
        if a[i]%x==0:
            c+=1
    if c == n:
        print(-1)
        continue
    a = a[::-1]
    sf = []
    sf.append(a[0])
    for i in range(1,n):
        sf.append(a[i]+sf[i-1])
    a = a[::-1]
    sf = sf[::-1]
    p.append(a[0])
    for i in range(1,n):
        p.append(a[i]+p[i-1])
    ans = 0
    l = 0
    r = n-1
    for i in range(n):
        if sf[i]%x!=0 and ans < n-1:
            l = i
            r = n-1
            ans = max(ans, n-i)
        if p[i]%x!=0 and ans < i+1:
            l = 0
            r = i
            ans = max(ans,i+1)
    print(ans)
