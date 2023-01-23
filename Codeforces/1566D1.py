import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(m):
        b.append((a[i],-i))
    b.sort()
    has = [0]*m
    ans = 0
    for _, i in b:
        i = -i
        for j in range(i):
            ans += has[j]
        has[i] += 1
    print(ans)
