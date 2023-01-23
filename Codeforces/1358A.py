import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    print(ceil((n*m)/2))
