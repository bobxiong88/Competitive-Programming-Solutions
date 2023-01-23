import sys
input = sys.stdin.readline
n, q = map(int,input().split())
a = list(map(int,input().split()))
curr = a[0]
change = dict()
res = 0
for i in range(n):
    change[i] = a[i]
    res += a[i]
for i in range(q):
    qry = list(map(int,input().split()))
    if len(qry) == 3:
        i,x = qry[1:]
        i-=1
        if i in change:
            res += x-change[i]
        else:
            res += x-curr
        change[i] = x
    else:
        x = qry[1]
        res = x*n
        curr = x
        change = dict()
    print(res)
    
