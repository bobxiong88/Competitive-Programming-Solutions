import sys
input = sys.stdin.readline
from itertools import *
n = int(input())
k = int(input())
ans = 0
cond = [tuple(map(int,input().split())) for i in range(k)]
for p in permutations([i for i in range(1,n+1)]):
    pos = [0]*(n+1)
    for i in range(n):
        pos[p[i]] = i
    res = True
    for a, b in cond:
        if pos[a] > pos[b]:
            res = False
            break
    ans += int(res)
print(ans)