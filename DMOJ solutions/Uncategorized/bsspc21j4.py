import sys
input = sys.stdin.readline
from heapq import *
X, N = map(int,input().split())
sup = []
mx = 0
for i in range(N):
    t, f = map(int,input().split())
    mx = max(f,mx)
    a = max(0, t-X)
    if a > f:
        continue
    sup.append((a,f))
sup.sort(reverse = True)
queue = []
heapify(queue)
ans  = 0
#print(sup)
for i in range(mx+1):
    while sup and sup[-1][0] <= i:
        a, b = sup.pop()
        heappush(queue, (b, a))
    while queue:
        b, a = heappop(queue)
        if b < i:
            continue
        #print(a,b)
        ans += 1
        break
print(ans)