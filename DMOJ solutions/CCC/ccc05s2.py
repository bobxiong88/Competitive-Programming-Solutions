import sys
input = sys.stdin.readline
c,r = map(int,input().split())
a,b = 0,0
while True:
    x,y = map(int,input().split())
    if not x and not y: break
    a+=x
    b+=y
    if a > c: a = c
    if a < 0: a = 0
    if b > r: b = r
    if b < 0: b = 0
    print a,b