import sys
input = sys.stdin.readline
from math import ceil
N, M = map(int,input().split())
ans = []
for i in range(1,M+1):
    a = N*(i-1)/M
    b = N*i/M
    for k in range(int(a)+1, ceil(b)+1):
        ans.append((k,i))
ans.sort()
print(len(ans))
for i in ans:print(*i)