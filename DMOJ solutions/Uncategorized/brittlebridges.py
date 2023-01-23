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
def dfs(node, p):
    res = 0
    for n in graph[node]:
        if n == p: continue
        res = max(res, dfs(n, node))
    return res+sz[node]
N = int(input())
sz = [0]+list(map(int,input().split()))
temp = [[] for i in range(N+1)]
par = [i for i in range(N+1)]
graph = [set() for i in range(N+1)]
for i in range(N-1):
    a, b, t = map(int,input().split())
    if t == 1:
        temp[a].append(b)
        temp[b].append(a)
    else:
        join(a, b)
for node in range(N+1):
    for n in temp[node]:
        n = find(n)
        graph[find(node)].add(n)
        graph[n].add(find(node))
print(dfs(find(1),find(1)))