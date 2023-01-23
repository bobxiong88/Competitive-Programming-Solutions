import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n,s = map(int,input().split())
    k = n//2+1
    print(s//k)
        
