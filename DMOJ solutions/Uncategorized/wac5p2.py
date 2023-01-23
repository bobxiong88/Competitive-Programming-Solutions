import sys
input = sys.stdin.readline
from collections import deque
n, q = map(int,input().split())
a = list(map(int,input().split()))
query = []
for i in range(q):
    x,y = map(int,input().split())
    query.append((max(x+y,x-y),min(x+y,x-y), i))
large = [0]*(n)
small = [0]*(n)
l = a[-1]
s = a[-1]
for i in range(-1, -n-1, -1):
    if a[i]>=l: l = a[i]
    large[i] = l
    if a[i]<=s: s = a[i]
    small[i] = s
ans = [0]*q
queue = list(reversed(sorted(query, key = lambda z: z[1])))
for i in range(n):
    while queue and queue[-1][1]<=small[i]:
        x,y,e = queue.pop()
        ans[e] = n-i
while queue:
    x,y,e = queue.pop()
    ans[e] = 0
queue = sorted(query, key = lambda z: z[0])
for i in range(n):
    while queue and queue[-1][0]>=large[i]:
        x,y,e = queue.pop()
        ans[e] = min(ans[e],n-i)
while queue:
    x,y,e = queue.pop()
    ans[e] = 0
for i in ans: print(i)