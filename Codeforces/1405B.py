import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    neg = []
    
    for i in range(n):
        if a[i] and a[i]//abs(a[i])!=1:
            neg.append([a[i], i])
    for i in range(n-1,-1,-1):
        if a[i] and a[i]//abs(a[i])==1:
            while neg and neg[-1][1] > i and a[i]!=0:
                if abs(neg[-1][0]) > a[i]:
                    neg[-1][0] += a[i]
                    a[i] = 0
                else:
                    a[i]+=neg[-1][0]
                    neg.pop()
    s = 0
    for i in neg: s+=i[0]
    print(-s)
    
                
    
