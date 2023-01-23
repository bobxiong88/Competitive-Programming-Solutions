import sys
sys.setrecursionlimit(100005)
input = sys.stdin.readline
def top(node):
    vis[node] = True
    for n in graph[node]:
        if not vis[n]:
            top(n)
    order.append(node)
N, M  = map(int,input().split())
dp = [0 for i in range(N+1)]
graph = [[] for i in range(N+1)]
vis = [False for i in range(N+1)]
order = []
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
for i in range(1,N+1):
    if not vis[i]: top(i)
order = order[::-1]
for node in order:
    for n in graph[node]:
        dp[n] = max(dp[n],dp[node]+1)
print(max(dp))