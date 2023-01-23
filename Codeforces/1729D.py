import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    pls = []
    neg = []
    for i in range(n):
        if y[i] >= x[i]:
            pls.append(y[i]-x[i])
        else:
            neg.append(x[i]-y[i])
    pls.sort()
    neg.sort()
    i = 0
    j = 0
    ans = 0
    while i < len(pls) and j < len(neg):
        if pls[i] >= neg[j]:
            ans += 1
            i += 1
            j += 1
        else:
            i += 2
            if i <= len(pls):
                ans += 1
    if i < len(pls):
        ans += (len(pls)-i)//2
    print(ans)
    
            
    
