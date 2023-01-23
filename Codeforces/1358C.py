import sys
from math import factorial as f
input = sys.stdin.readline
def tri(n):
    return(n*(n+1)//2)
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    x,y = min(x2-x1,y2-y1), max(x2-x1,y2-y1)
    if not x or not y:
        print(1)
        continue
    ans = tri(x-1)*2+x*(y-x+1)
    print(ans+1)
    #print(xd,yd,t)
