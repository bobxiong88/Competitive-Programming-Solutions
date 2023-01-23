import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,a,b = map(int,input().split())
    g = [[] for i in range(n+1)]
    for i in range(n-1):
        u,v,w = map(int,input().split())
        g[u].append((v,w))
        g[v].append((u,w))
    fa = [0]
    fb = []
    def dfs(u, p, x, vals, dis):
        for v,w in g[u]:
            if v == p: continue
            if v == dis: continue
            dfs(v, u, w^x, vals, dis)
            vals.append(w^x)
    dfs(a, a, 0, fa, b)
    dfs(b, b, 0, fb, -1)
    s = set(fb)
    ans = "NO"
    for i in fa:
        if i in s:
            ans = "YES"
            break
    print(ans)
            
