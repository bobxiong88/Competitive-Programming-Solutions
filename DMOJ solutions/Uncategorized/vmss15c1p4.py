import sys
from collections import deque
input = sys.stdin.readline
T, N, M, G = map(int,input().split())
graph = {}
for i in range(N+1):
    graph.update({i:{}})
banks = []
for i in range(G):
    banks.append(int(input()))
for i in range(M):
    a,b,l = map(int,input().split())
    graph[a].update({b:l})
dist = [float('inf')]*(N+1)
dist[0] = 0
queue = deque([(0,0)])
while queue:
    node, d = queue.popleft()
    if d > dist[node]:
        continue
    for n in graph[node]:
        c = d + graph[node][n]
        if dist[n] > c and c <= T:
            dist[n] = c
            queue.append((n,c))
c = 0
for b in banks:
    if dist[b] <= T:
        c+=1
print(c)