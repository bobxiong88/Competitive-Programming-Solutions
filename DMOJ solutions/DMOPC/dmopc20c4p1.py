import sys
from math import *
input = sys.stdin.readline
for _ in range(int(input())):
    N, S = map(int,input().split())
    tot = N*(N+1)//2
    r = tot-S
    low = r//2+1
    high = min(N,r-1)
    ans = high-low+1
    if ans < 0:
        print(0)
    else:
        print(ans)