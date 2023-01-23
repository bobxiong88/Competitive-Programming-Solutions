import sys
input = sys.stdin.readline
def find(v):
    if par[v] == v: return v
    par[v] = find(par[v])
    return par[v]
def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return
    if sz[a] < sz[b]: a,b = b,a
    par[b] = a
    sz[a] += sz[b]
N, Q = map(int,input().split())
par = [i for i in range(N+1)]
sz = [1 for i in range(N+1)]
for i in range(Q):
    A, x, y = input().split()
    x, y = int(x), int(y)
    if A == 'A':
        union(x,y)
    else:
        print('Y' if find(x) == find(y) else 'N')