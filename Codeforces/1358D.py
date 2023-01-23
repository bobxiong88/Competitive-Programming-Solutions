import sys
from collections import deque
input = sys.stdin.readline
def t(n):
    return n*(n+1)//2
n,x = map(int,input().split())
d = list(map(int,input().split()))
tw = 0
tv = 0
ans = -1
queue = deque([])
for i in range(-1,-n-1,-1):
    queue.appendleft(d[i])
    tw += d[i]
    tv += t(d[i])
    if tw>=x: break
for i in range(n):
    tw += d[i]
    tv += t(d[i])
    queue.append(d[i])
    c = int(tv)
    while tw>x:
        curr = queue.popleft()
        tw-=curr
        tv-=t(curr)
        c-=t(curr)
    c += t(curr) - t(curr-(x-tw))
    ans = max(c,ans)
print(ans)
