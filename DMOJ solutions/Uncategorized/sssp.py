import sys
input = sys.stdin.readline
import heapq
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
dist  = [float('inf') for i in range(N+1)]
dist[1] = 0
queue = [(0,1)]
while queue:
    d, node = heapq.heappop(queue)
    if d > dist[node]:
        continue
    for n, w in graph[node]:
        if dist[n] > d + w:
            dist[n] = d + w
            heapq.heappush(queue, (d+w, n))
for i in range(1,N+1):
    print(-1 if dist[i] == float('inf') else dist[i])