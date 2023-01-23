import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    c = int(input())
    b = int(input())
    a = int(input())
    if a+b+c<n:
        print(-1)
        continue
    res = []
    res.append(min(a,n))
    n -= min(a,n)
    res.append(min(b,n))
    n -= min(b,n)
    res.append(min(c,n))
    res = res[::-1]
    print res[0], res[1], res[2]