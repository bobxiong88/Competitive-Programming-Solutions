import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    a,b,c = sorted([a,b,c])
    x = ((c-a)**2+b**2)**0.5
    print(ceil(x))
