import sys
input = sys.stdin.readline
def dfs(node, p):
    for n in graph[node]:
        if n == p: continue
        size[node] += dfs(n, node)
    return size[node]
n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
size = [1 for i in range(n+1)]
dfs(1, -1)
ans = (1, float('inf'))
for node in range(1,n+1):
    m = -1
    for v in graph[node]:
        if size[v] > size[node]: m = max(m, size[1]-size[node])
        else: m = max(m, size[v])
    if m < ans[1]: ans = (node, m)
print ans[0],ans[1]