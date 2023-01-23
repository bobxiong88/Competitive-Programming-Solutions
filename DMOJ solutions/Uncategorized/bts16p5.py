import sys
input = sys.stdin.readline
sys.setrecursionlimit(10005)
def dfs(node, p):
    for n,w in graph[node]:
        if n == p: continue
        dfs(n, node)
        edge[node] += edge[n]+w
        sz[node] += sz[n]
N, C, K = map(int,input().split())
sz = [0]+list(map(int,input().split()))
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a,b,k = map(int,input().split())
    graph[a].append((b,k))
    graph[b].append((a,k))
edge = [0]*(N+1)
dfs(1,1)
ans = 0
vis = [False]*(N+1)
for node in range(1,N+1):
    for n,w in graph[node]:
        if vis[n]: continue
        vis[n] = True
        if sz[n] >= C and edge[n]+w<=K:
            ans += 1
print(ans)