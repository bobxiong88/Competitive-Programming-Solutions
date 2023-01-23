import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)
def dfs(node, p):
    global ans
    path = []
    for n in graph[node]:
        if n == p: continue
        dfs(n, node)
        dp[node] = max(dp[node], dp[n]+1)
        path.append(dp[n]+1)
    path.sort(reverse = True)
    if len(path)==0:
        pass
    elif len(path)==1:
        ans = max(path[0],ans)
    else:
        ans = max(path[0]+path[1], ans)
N = int(input())
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dp = [0]*(N+1)
ans = 0
dfs(1,1)
print(ans)