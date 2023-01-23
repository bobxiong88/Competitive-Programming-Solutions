import sys
input = sys.stdin.readline
def find(v):
    if par[v] == v: return v
    par[v] = find(par[v])
    return par[v]
def join(a, b):
    a, b = find(a), find(b)
    if a == b: return False
    if sz[a] < sz[b] : a, b = b, a
    sz[a] += sz[b]
    par[b] = a
    return True
N, M = map(int,input().split())
a = list(map(int,input().split()))
par = [i for i in range(N+1)]
sz = [1 for i in range(N+1)]
for i in range(M):
    x, y = map(int,input().split())
    join(x, y)
edge = []
for i in range(N-1):
    edge.append((a[i+1]-a[i], i+1, i+2))
edge.sort()
ans = 0
for v, x, y in edge:
    if join(x,y):
        ans += v
print(ans)