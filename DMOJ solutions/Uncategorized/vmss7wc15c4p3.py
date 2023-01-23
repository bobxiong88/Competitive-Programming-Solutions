import sys
from collections import deque
def bfs(start):
    dist = [float('inf')]*N
    queue = deque([start])
    dist[start] = 0
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if graph[node][n] + dist[node] < dist[n]:
                dist[n] = graph[node][n] + dist[node]
                queue.append(n)
    return dist
input = sys.stdin.readline
N, M = map(int,input().split())
graph = {}
for i in range(N):
    graph.update({i:{}})
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].update({b:c})
    graph[b].update({a:c})
one = bfs(0)
two = bfs(N-1)
m = -1
for i in range(N):
    m = max(m, one[i]+two[i])
print(m)