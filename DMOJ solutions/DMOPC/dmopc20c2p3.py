import sys
input = sys.stdin.readline
def top(node):
    vis[node] = True
    for n in graph[node]:
        if not vis[n]:
            top(n)
    order.append(node)
N = int(input())
a = [0]+list(map(int,input().split()))
dp = a[:]
dp2 = a[:]
graph = [[] for i in range(N+1)]
edges = []
for i in range(N-1):
    u,v = map(int,input().split())
    edges.append((u,v))
    graph[u].append(v)
order = []
vis = [False for i in range(N+1)]
for i in range(1, N+1):
    if not vis[i]:
        top(i)
ans = 0
for node in order:
    for n in graph[node]:
        dp[node] += dp[n]
    ans += a[node]*(dp[node]-1)
for node in order[::-1]:
    for n in graph[node]:
        dp2[n] += dp2[node]
res = 0
for u,v in edges:
    res = max(res,(dp[u]-dp[v])*(dp2[v]-dp2[u]))
print(ans+res)