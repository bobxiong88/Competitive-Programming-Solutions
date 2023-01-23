# step one: find required blue edges
# make graph with only red edge by dsu
# iterate through all blue edges, if blue edges connect two different components i.e. different parent (parent array start off as themselves), connect them (union dsu)
# if there are more than k blue edges, its impossible

# step two: add new blue edges
# make graph with only the blue edges from before by dsu
# iterate through blue edges, if they connect two differnet components, dsu them, do until we have K edges
# add red edges greedily through dsu
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
N, M, K = map(int,input().split())
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
cobbles = []
concretes = []
ans = []
for i in range(M):
    u,v,c = map(int,input().split())
    if not c:
        cobbles.append((u,v,c))
    else:
        concretes.append((u,v,c))
for u,v,i in concretes:
    if find(u)!=find(v):
        union(u,v)
count = 0
for u,v,c in cobbles:
    if find(u)!=find(v):
        count+=1
        union(u,v)
        ans.append((u,v,c))
if count > K:
    print("no solution")
    sys.exit(0)
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
for u,v,c in ans:
    union(u,v)
for u,v,c in cobbles:
    if find(u)!=find(v):
        count+=1
        union(u,v)
        ans.append((u,v,c))
        if count >= K:
            break
if count < K:
    print("no solution")
    sys.exit(0)
for u,v,c in concretes:
    if find(u)!=find(v):
        union(u,v)
        ans.append((u,v,c))
        if len(ans) == N-1:
            break
for u,v,c in ans:
    print u,v,c