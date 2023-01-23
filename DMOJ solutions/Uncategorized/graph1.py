import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
X, Y = map(int,input().split())
vis = [False]*(N+1)
vis[X] = True
queue = deque([X])
while queue:
    node = queue.popleft()
    if node == Y:
        print(1)
        sys.exit(0)
    for n in graph[node]:
        if not vis[n]:
            vis[n] = True
            queue.append(n)
print(0)