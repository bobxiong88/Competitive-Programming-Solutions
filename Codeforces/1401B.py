import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x1,y1,z1 = map(int,input().split())
    x2,y2,z2 = map(int,input().split())
    ans = 0
    m=min(x1,z2)
    x1-=m
    z2-=m

    m=min(y1,x2)
    y1-=m
    x2-=m
    
    ans += min(z1,y2)*2
    m = min(z1,y2)
    z1-=m
    y2-=m
    
    ans-=min(z2,y1)*2
    
    print(ans)
