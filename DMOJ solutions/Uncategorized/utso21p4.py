import sys
input = sys.stdin.readline
def find(v):
    if v == par[v]: return v
    par[v] = find(par[v])
    return par[v]
def join(a, b):
    a, b = find(a), find(b)
    if a == b: return False
    if sz[a] < sz[b]: a, b = b, a
    sz[a] += sz[b]
    par[b] = a
    return True
def dfs(node, p):
    vis[node] = True
    d = 0
    for n, idx in graph[node]:
        if n == p: continue
        if dfs(n, node): d += 1
        else: ans.append(idx)
    if d % 2 == 0:
        return True
    else:
        return False
N, M = map(int,input().split())
par = [i for i in range(N+1)]
sz = [1 for i in range(N+1)]
graph = [[] for i in range(N+1)]
vis = [False]*(N+1)
ans = []
luck = 0
for i in range(M):
    a, b = map(int,input().split())
    if join(a, b):
        graph[a].append((b, i))
        graph[b].append((a, i))
    else:
        ans.append(i)
for node in range(1,N+1):
    if not vis[node]:
        node = find(node)
        dfs(node, node)
        luck += sz[node]-sz[node]%2
print(luck)
print(len(ans))
ans.sort()
print(' '.join([str(i+1) for i in ans]))