# observation: answer always highest degree from original graph
# bfs from the node with maximum degree
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
g = [[] for i in range(n+1)]
deg = [0]*(n+1)
for i in range(m):
    u, v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1
high = (0, 0)
for i in range(1,n+1): high = max(high, (deg[i], i))
queue = deque([high[1]])
res = []
vis = [False]*(n+1)
vis[high[1]] = True
while queue:
    u = queue.popleft()
    for v in g[u]:
        if not vis[v]:
            queue.append(v)
            res.append((u,v))
            vis[v] = True
for edge in res:
    print(*edge)


