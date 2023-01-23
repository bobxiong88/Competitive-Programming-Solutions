import sys
input = sys.stdin.readline
def find(v):
    if v==parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]
def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
        if rank[a] < rank[b]:
            a,b = b, a
        parent[b] = a
        if rank[a]==rank[b]:
            rank[a]+=1
N, M, D = map(int,input().split())
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
edges = []
big = 0
for i in range(M):
    u,v,w = map(int,input().split())
    old = False
    if i<N-1:
        old = True
    edges.append([u,v,w,old])
edges.sort(key = lambda x: x[2])
d = 0
for i in range(M):
    u,v,w,old = edges[i]
    if find(u)!=find(v):
        union(u,v)
        big = max(w,big)
        if not old: d+=1
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
for edge in edges:
    u,v,w,old = edge
    if find(u)!=find(v):
        if w < big or (old and w==big):
            union(u,v)
        elif w <= D and old:
            union(u,v)
            d-=1
            break
print(d)