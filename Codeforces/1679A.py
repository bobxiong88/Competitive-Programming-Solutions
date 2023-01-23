import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    if n < 4 or n%2:
        print(-1)
    else:
        b = n//4
        a = n//6
        if n%6: a += 1
        print(a,b)
