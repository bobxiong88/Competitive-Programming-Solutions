import sys
input = sys.stdin.readline
def find(v):
    if v==parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]
def union(a, b):
    a, b = find(a), find(b)
    if a == b: return False
    if size[a] < size[b]:
        a,b = b, a
    parent[b] = a
    size[a] += size[b]
    return True
N, M = map(int,input().split())
parent = [i for i in range(N+1)]
size = [1]*(N+1)
edges = []
for i in range(1,M+1):
    u,v = map(int,input().split())
    if union(u, v):
        edges.append(i)
if len(edges)<N-1:
    print("Disconnected Graph")
    sys.exit(0)
for i in edges: print(i)