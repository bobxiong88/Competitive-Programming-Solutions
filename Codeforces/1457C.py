import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,p,k = map(int,input().split())
    a = list(map(int,list(input().strip('\n'))))
    x,y = map(int,input().split())
    ans = float('inf') 
    for i in range(-1+k,-k-1+k,-1):
        c = 0
        while i-k-p+1>=-n:
            v = 0
            if i<0:
                if not a[i]: c += x
            if not a[i-k]: v += x
            v += y*(n+i-k-p+1)
            ans = min(ans, c+v)
            #print(n+i-k-p+1,v,c+v)
            i -= k
            #print(i, c)
    print(ans)
