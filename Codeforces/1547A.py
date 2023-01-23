import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    xa,ya = map(int,input().split())
    xb,yb = map(int,input().split())
    xf,yf = map(int,input().split())
    d = abs(xa-xb)+abs(ya-yb)
    if xa == xb == xf and min(ya, yb) < yf < max(ya, yb):
        d += 2
    elif ya == yb == yf and min(xa, xb) < xf < max(xa, xb):
        d += 2
    print(d)

