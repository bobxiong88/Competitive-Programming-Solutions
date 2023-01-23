import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    lp = 0
    s = 0
    for i in range(m):
        s += b[i]
        lp = max(lp, s)
    ans = lp
    s = 0
    lp2 = 0
    for i in range(n):
        s += r[i]
        lp2 = max(s, lp2)
        ans = max(ans, s+lp)
    ans = max(ans, lp2)
    s = 0
    for i in range(m):
        s += b[i]
        ans = max(ans, s+lp2)
    print(ans)
            
