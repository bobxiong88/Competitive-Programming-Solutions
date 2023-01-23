import sys
input = sys.stdin.readline
def top(node):
    vis[node] = True
    for n, w in graph[node]:
        if not vis[n]:
            top(n)
    order.append(node)
def cycle(node):
    vis[node] = True
    stack[node] = True
    for n, w in graph[node]:
        if not vis[n]:
            if cycle(n):
                return True
        elif stack[n]:
            return True
    stack[node] = False
    return False
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
vis = [False]*(N+1)
stack = [False]*(N+1)
for node in range(1,N+1):
    if not vis[node]:
        if cycle(node):
            print(-1)
            sys.exit(0)
vis = [False]*(N+1)
order = []
for node in range(1,N+1):
    if not vis[node]:
        top(node)
order = order[::-1]
dp = [[0,1] for i in range(N+1)]
for node in order:
    for n, w in graph[node]:
        dp[n] = max(dp[n], [dp[node][0]+w,dp[node][1]+1])
if dp[N] == [0,1]:
    print(-1)
else:
    print(*dp[N])