import sys
input = sys.stdin.readline
def ga(x):
    m = len(a)+x
    k = m-m//4
    if k <= m-n:
        return k*100
    else:
        s = (m-n)*100
        k -= m-n
        i = 0
        while k:
            s += a[i]
            k-=1
            i += 1
        return s
def gb(x):
    m = len(b)+x
    k = m-m//4
    s = 0
    if k > len(b):
        return sum(b)
    else:
        for i in range(k):
            s += b[i]
        return s
def bs(l, r):
    if ga(l) >= gb(l):
        return l
    while l <= r:
        m = (l+r)//2
        if ga(m) >= gb(m) and ga(m-1) < gb(m-1):
            return m
        if ga(m) < gb(m):
            l = m+1
        else:
            r = m-1
    return 0/0
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse = True)
    b.sort(reverse = True)
    #print(a, b)
    
    print(bs(0, n))
