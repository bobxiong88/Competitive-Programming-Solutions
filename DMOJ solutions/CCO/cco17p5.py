import sys
input = sys.stdin.readline
import heapq
N = int(input())
a= []
for i in range(N):
    x, y = map(int,input().split())
    a.append((x,-y))
a.sort()
queue = []
cnt = 0
ans = 0
heapq.heapify(queue)
for m in range(N-1, -1, -1):
    x, y = a[m]
    y = -y
    m = x-m-cnt
    heapq.heappush(queue,y)
    while queue and m > 0:
        m-=1
        ans += heapq.heappop(queue)
        cnt+=1
print(ans)