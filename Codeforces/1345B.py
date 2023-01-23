import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())
    ans = 0
    while True:
        pre = x
        n = int((-1+(1+24*x)**0.5)/6)
        x-=(3*(n**2)+n)/2
        if pre==x or x<0:
            break
        ans+=1
    print(ans)
        
        
