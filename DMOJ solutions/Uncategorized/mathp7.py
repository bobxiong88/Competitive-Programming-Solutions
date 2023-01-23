import sys
from math import *
input = sys.stdin.readline
def cnt(N):
    res = 0
    for i in range(1,N+1):
        if N%i == 0: res += 1
    return res
def f(N):
    res = 0
    for i in range(1,N+1):
        res += cnt(i)
    return res
N = int(input())
ans = 0
for i in range(1, floor(sqrt(N))+1):
    ans += 2*floor(N/i)
ans -=floor(sqrt(N))**2
print(ans)