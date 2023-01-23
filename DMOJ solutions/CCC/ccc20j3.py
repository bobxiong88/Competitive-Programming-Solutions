import sys
input = sys.stdin.readline
N = int(input())
minx, miny = [float('inf')]*2
maxx, maxy = [-float('inf')]*2
for i in range(N):
    x,y = map(int,input().split(','))
    minx = min(x, minx)
    maxx = max(x, maxx)
    miny = min(y, miny)
    maxy = max(y, maxy)
print("{},{}".format(minx-1, miny-1))
print("{},{}".format(maxx+1, maxy+1))