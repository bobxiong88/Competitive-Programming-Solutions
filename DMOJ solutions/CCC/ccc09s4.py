import sys
from heapq import *
input = sys.stdin.readline
N = int(input())
T = int(input())
graph = [[0]*(N+1) for i in range(N+1)]
for i in range(T):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
K = int(input())
cost = [999999]*(N+1)
m = 10005
for i in range(K):
    n, p = map(int,input().split())
    cost[n] = p
    m = min(m, p)
D = int(input())
queue = [(0, D)]
heapify(queue)
dist = [999999]*(N+1)
dist[D] = 0
ans = 999999999
out = [False]*(N+1)
while queue:
    d, node = heappop(queue)
    if d > dist[node]: continue
    if d+m >= ans-155: continue
    ans = min(ans, cost[node]+d)
    for n,w in enumerate(graph[node]):
        if not w: continue
        current = d + w
        if dist[n]>current:
            dist[n] = current
            heappush(queue, (current, n))
print(ans)