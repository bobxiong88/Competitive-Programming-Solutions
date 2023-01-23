import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    t = list(map(int,input().split()))
    l = min(x)
    r = max(x)
    
    for _ in range(30):
        m = (l+r)/2
        left = 0
        right = 0
        
        for i in range(n):
            if x[i] <= m:
                left = max(left,m-x[i]+t[i])
            else:
                right = max(right,x[i]-m+t[i])
        #print(m,left,right)
        if left < right:
            l = m
        else:
            r = m
    print(m)
    
