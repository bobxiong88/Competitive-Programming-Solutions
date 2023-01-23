import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    ans = 0
    if abs(x2-x1):
        ans += abs(x2-x1)
        if abs(y2-y1):
            ans += abs(y2-y1)+2
    elif abs(y2-y1):
        ans += abs(y2-y1)
    print(ans)
    
    
