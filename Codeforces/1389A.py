import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    l,r = map(int,input().split())
    x = l
    y = l*2
    if y>r:
        print(-1,-1)
        continue
    print(x,y)
    
