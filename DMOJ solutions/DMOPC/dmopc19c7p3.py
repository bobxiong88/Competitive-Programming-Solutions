import sys
input = sys.stdin.readline
def dfs(node):
    global w
    curr.append(node)
    vis[node] = True
    w += a[node]
    if k <= w:
        print(len(curr))
        print(*curr)
        sys.exit(0)
    for v in graph[node]:
        if not vis[v]:
            dfs(v)
n, k = map(int,input().split())
a = [0]+list(map(int,input().split()))
vis = [False]*(n+1)
graph = [[] for i in range(n+1)]
for i in range(1,n+1):
    if k <= a[i] <= 2*k:
        print(1)
        print(i)
        sys.exit(0)
    if a[i] > 2*k:
        vis[i] = True
for i in range(n-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for node in range(1,n+1):
    if not vis[node]:
        curr = []
        w = 0
        dfs(node)
print(-1)