import sys
input = sys.stdin.readline
from collections import deque
def bfs(node):
    queue = deque([node])
    vis[node] = True
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not vis[n]:
                vis[n] = True
                queue.append(n)
n,m,q = map(int,input().split())
graph = [[] for i in range(n+1)]
vis = [False]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
bfs(1)
for i in range(q):
    line = input().split()
    if line[0] == '+':
        a,b = map(int,line[1:])
        graph[a].append(b)
        if vis[a] and not vis[b]:
            bfs(b)
    else:
        a = int(line[1])
        print('YES' if vis[a] else 'NO')