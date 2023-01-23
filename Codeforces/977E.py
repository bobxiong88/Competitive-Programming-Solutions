import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)
c = 0
for i in range(1, n+1):
    if not visited[i]:
        found = True
        queue = deque([i])
        visited[i] = True
        while queue:
            node = queue.popleft()
            if len(graph[node])!=2:found = False
            for n in graph[node]:
                if not visited[n]:
                    queue.append(n)
                    visited[n] =  True
        if found: c+=1
print(c)
