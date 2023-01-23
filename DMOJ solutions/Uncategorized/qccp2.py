import sys
input = sys.stdin.readline
N = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)
Q = int(input())
for i in range(Q):
    t,w = map(int,input().split())
    if t == 1:
        print(max(ymax,x[w-1]))
    elif t == 2:
        print(max(ymin,x[w-1]))
    elif t == 3:
        print(max(xmax,y[w-1]))
    else:
        print(max(xmin,y[w-1]))