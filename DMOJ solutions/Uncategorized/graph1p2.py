import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n)]
for i in range(n):
    for j,x in enumerate(list(map(int,input().split()))):
        if x and j>i:
            graph[i].append(j)
            graph[j].append(i)
queue = deque([0])
dist = [float('inf')]*(n)
dist[0] = 0
while queue:
    node = queue.popleft()
    for v in graph[node]:
        if dist[v] > dist[node]+1:
            dist[v] = dist[node]+1
            queue.append(v)
print(dist[n-1])