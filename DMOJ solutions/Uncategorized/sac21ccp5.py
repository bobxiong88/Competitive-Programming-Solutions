import sys
input = sys.stdin.readline
def find(v):
    if par[v] == v: return v
    par[v] = find(par[v])
    return par[v]
def join(a,b):
    a = find(a)
    b = find(b)
    if a == b: return
    sz[a] += sz[b]
    par[b] = a
N, Q = map(int,input().split())
par = [i for i in range(N+1)]
sz = [1 for i in range(N+1)]
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        u,v = list(map(int,q[1:]))
        join(u,v)
    else:
        x = int(q[1])
        print(sz[find(x)])