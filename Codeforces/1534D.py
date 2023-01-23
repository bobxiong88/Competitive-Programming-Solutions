import sys
input = sys.stdin.readline
def find(v):
    if v == par[v]: return v
    par[v] = find(par[v])
    return par[v]
def join(a, b):
    a, b = find(a), find(b)
    if a==b:return
    if sz[a] < sz[b]: a, b = b, a
    sz[a] += sz[b]
    par[b] = a
def ext(v):
    if find(v) == find(1): return True
    return False
def qry(x):
    print("? {}".format(x))
    sys.stdout.flush()
    return [0]+list(map(int,input().split()))
n = int(input())
if n == 2:
    print("!")
    print("1 2")
    sys.stdout.flush()
    sys.exit(0)
par = [i for i in range(n+1)]
sz = [1 for i in range(n+1)]
dist = qry(1)
ans = []
layer = [[] for i in range(n+1)]
for i in range(1,n+1):
    layer[dist[i]].append(i)
for i in range(n, 0, -1):
    while layer[i]:
        v = layer[i].pop()
        if ext(v): continue
        d2 = qry(v)
        p = 1
        for j in range(1,i):
            for u in layer[j]:
                if d2[u]+dist[u] == dist[v]:
                    join(p, u)
                    ans.append((p,u))
                    p = u
                    break
        join(p, v)
        ans.append((p,v))
        for u in layer[i]:
            if d2[u] == 2:
                join(p,u)
                ans.append((p,u))
new = set()
for a,b in ans:
    new.add((min(a,b),max(a,b)))
print('!')
for i in new:
    print(*i)
sys.stdout.flush()
