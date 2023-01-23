import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
k = int(input())
dist = [float('inf')]*(n+1)
queue = deque([])
dist[0] = 0
for i in range(k):
    a = int(input())
    dist[a] = 0
    queue.append(a)
while queue:
    node = queue.popleft()
    for n in graph[node]:
        if dist[n] > dist[node] + 1:
            dist[n] = dist[node]+1
            queue.append(n)
print(max(dist))