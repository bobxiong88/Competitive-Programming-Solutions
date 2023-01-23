import sys
from collections import deque
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
N, K = map(int,input().split())
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
w = tuple(list(map(int,input().split())))
george = []
for i in range(1,N+1):
    if i+K<=N:
        george.append((i,i+K))
    else:
        break
floyd = []
for i in range(N):
    if i+2<=N:
        floyd.append((i+1,i+2,w[i]))
for u,v in george:
    union(u,v)
floyd.sort(key = lambda x: x[2])
t = 0
for u,v,e in floyd:
    if find(u)!=find(v):
        union(u,v)
        t+=e
print(t)