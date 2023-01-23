import sys
input = sys.stdin.readline
for _ in range(int(input())):
    r,g,b,w = map(int,input().split())
    mx = min(r,g,b)
    w += mx*3
    r-=mx
    g-=mx
    b-=mx
    arr = [r%2, g%2, b%2, w%2]
    inverse = [1]*4
    if mx>=1:
        inverse = [1-i for i in arr]
    if arr.count(1)>1 and inverse.count(1)>1:
        print("No")
    else:
        print("Yes")
