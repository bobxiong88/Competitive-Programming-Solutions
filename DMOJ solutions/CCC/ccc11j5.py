import sys
input = sys.stdin.readline
def dfs(node, p):
    for n in graph[node]:
        if n == p: continue
        dfs(n, node)
        dp[node] *= dp[n]+1
N = int(input())
graph = [[] for i in range(N+1)]
for i in range(1,N):
    j = int(input())
    graph[j].append(i)
    graph[i].append(j)
dp = [1]*(N+1)
dfs(N, N)
print(dp[N])