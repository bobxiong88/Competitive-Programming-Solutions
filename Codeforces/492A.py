import sys
from math import ceil
input = sys.stdin.readline
n = int(input())
ans = 0
s = 0
for i in range(1,n+1):
    s += i*(i+1)/2
    if s > n:
        break
    ans += 1
    
print(ans)
