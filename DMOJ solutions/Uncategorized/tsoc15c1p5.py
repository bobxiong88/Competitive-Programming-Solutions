import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph = {}
for i in range(1,N+1):
    graph.update({i:[]})
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
W = int(input())
ants = []
dist = [float('inf')]*(N+1)
for i in range(W):
    wi = int(input())
    ants.append(wi)
    dist[wi] = 0
queue = deque(ants)
while queue:
    node = queue.popleft()
    for n in graph[node]:
        if dist[n] > dist[node]+1:
            dist[n] = dist[node]+1
            queue.append(n)
queue = deque([(1,0)])
visited = [False]*(N+1)
visited[1] = True
ans = float('inf')
while queue:
    node, d = queue.popleft()
    if dist[node] <= d//4:
        continue
    if node == N:
        print(d)
        sys.exit(0)
    for n in graph[node]:
        if not visited[n]:
            queue.append((n,d+1))
print("sacrifice bobhob314")