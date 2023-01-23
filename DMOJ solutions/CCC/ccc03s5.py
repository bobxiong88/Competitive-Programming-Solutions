import sys
sys.setrecursionlimit(10005)
input = sys.stdin.readline
def dfs(node, p):
    for n,w in graph[node]:
        if n == p: continue
        m[n] = min(m[node], w)
        dfs(n, node)
def find(v):
    if parent[v] == v: return v
    parent[v] = find(parent[v])
    return parent[v]
def join(a,b):
    a = find(a)
    b = find(b)
    if a == b: return False
    if sz[a] < sz[b]: a,b = b,a
    parent[b] = a
    sz[a] += sz[b]
    return True
c, r, d = map(int,input().split())
edges = [tuple(map(int,input().split())) for i in range(r)]
parent = [i for i in range(c+1)]
sz = [1 for i in range(c+1)]
edges.sort(key = lambda x: x[2], reverse = True)
ans = float('inf')
mst = []
graph = [[] for i in range(c+1)]
for x, y, w in edges:
    if join(x,y):
        mst.append((x,y,w))
        graph[x].append((y,w))
        graph[y].append((x,w))
m = [float('inf') for i in range(c+1)]
dfs(1,-1)
for i in range(d):
    n = int(input())
    ans = min(ans, m[n])
print(ans)