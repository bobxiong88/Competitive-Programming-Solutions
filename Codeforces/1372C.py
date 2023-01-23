import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.insert(0,0)
    start = False
    c = 0
    for i in range(1, n+1):
        if i!=a[i] and start==False:
            start = True
            c+=1
        if i==a[i] and start ==True:
            start=  False
    if c<2:
        print(c)
    else:
        print(2)
