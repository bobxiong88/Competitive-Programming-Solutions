import sys
input = sys.stdin.readline
def dfs(node):
    vis[node] = True
    for n in graph[node]:
        if not vis[n]: dfs(n)
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
edges = []
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    edges.append((a,b))
for a,b in edges:
    graph[a].remove(b)
    vis = [False]*(N+1)
    dfs(1)
    if vis[N]:
        print('YES')
    else:
        print('NO')
    graph[a].append(b)