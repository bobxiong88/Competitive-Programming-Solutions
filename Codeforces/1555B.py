import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    W, H = map(int,input().split())
    x1,y1,x2,y2 = map(int,input().split())
    w, h = map(int,input().split())
    ans = 0
    hor = float('inf')
    ver = float('inf')
    mw, mh = x2-x1, y2-y1
    if x1-w < 0:
        if w+mw <= W:
            hor = w-x1
    else:hor=0
    if x2+w > W:
        if x1-(x2-(W-w)) >= 0:
            hor = min(hor, x2-(W-w))
    else:hor = 0
    if y1-h < 0:
        if h+mh <= H:
            ver = h-y1
    else: ver=0
    if y2+h > H:
        if y1-(y2-(H-h)) >= 0:
            ver = min(ver, y2-(H-h))
    else: ver=0
    ans = min(hor,ver)
    if ans == float('inf'):ans = -1
    print(ans)
