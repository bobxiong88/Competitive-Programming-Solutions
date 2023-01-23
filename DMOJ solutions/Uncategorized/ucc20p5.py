import sys
from collections import deque
input = sys.stdin.readline
L, S, E, N  = map(int,input().split())
graph = [[] for i in range(L+1)]
for i in range(N):
    a, b = map(int,input().split())
    graph[a].append(b)
queue = deque([(S, 0)])
visited = [False]*(L+1)
visited[S] = True
while queue:
    node, d = queue.popleft()
    if node == E:
        print(d)
        sys.exit(0)
    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            queue.append((n, d+1))