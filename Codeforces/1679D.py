import sys
sys.setrecursionlimit(200005)
input = sys.stdin.readline
def cycle(u):
    vis[u] = True
    stack[u] = True
    for v in g[u]:
        if not vis[v]:
            if cycle(v):
                return True
        elif stack[v] == True:
            return True
    stack[u] = False
    return False
def top(u):
    vis[u] = True
    for v in g[u]:
        if not vis[v]:
            top(v)
    order.append(u)
def pos(x):
    for u,v in edges:
        if a[u] > x or a[v] > x: continue
        g[u].append(v)
    for i in range(1,n+1):
        if a[i] > x: continue
        if not vis[i]:
            if cycle(i):
                return True
    for i in range(n+1): vis[i] = False
    for i in range(1,n+1):
        if a[i] > x: continue
        if not vis[i]:
            top(i)
    order.reverse()
    dp = [-1]*(n+1)
    for u in order:
        dp[u] = max(dp[u],0)
        for v in g[u]:
            dp[v] = max(dp[v],dp[u]+1)
    if max(dp) >= k-1:
        return True
    return False
global n,m,k
n, m, k = map(int,input().split())
a = [0]+list(map(int,input().split()))
edges = [tuple(map(int,input().split())) for i in range(m)]
g = [[] for i in range(n+1)]
vis = [False]*(n+1)
stack = [False]*(n+1)
order = []
l = 1
r = int(1e9)
res = -1
while l <= r:
    m = (l+r)//2
    if pos(m):
        r = m-1
        res = m
    else:
        l = m+1
    order = []
    vis = [False]*(n+1)
    stack = [False]*(n+1)
    g = [[] for i in range(n+1)]
print(res)
