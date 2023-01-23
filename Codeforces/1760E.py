import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = [0]+list(map(int,input().split()))
    prevone = [0]*(n+1)
    sufzero = [0]*(n+2)
    for i in range(1,n+1):
        prevone[i] = a[i]+prevone[i-1]
    for i in range(n,0,-1):
        sufzero[i] = sufzero[i+1] + (a[i]==0)
    s = 0
    for i in range(1,n+1):
        if a[i] == 0: s+=prevone[i]
    ans = s
    for i in range(1,n+1):
        #print(ans,s)
        if a[i] == 0:
            ans = max(ans, s+sufzero[i+1]-prevone[i-1])
        else:
            ans = max(ans, s+prevone[i-1]-sufzero[i+1])
    print(ans)
