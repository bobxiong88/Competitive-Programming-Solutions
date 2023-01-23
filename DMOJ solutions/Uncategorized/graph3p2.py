import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
dist = [float('inf') for i in range(n+1)]
dist[1] = 0
queue = deque([1])
while queue:
    node = queue.popleft()
    for v,w in graph[node]:
        if dist[v] > dist[node]+w:
            dist[v] = dist[node]+w
            queue.append(v)
print(dist[n])