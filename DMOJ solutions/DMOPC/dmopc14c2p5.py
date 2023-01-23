import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = {}
for i in range (1, N+1):
    graph.update({i:[]})
for i in range(M):
    a,b = [int(i) for i in input().split()]
    graph[a].append(b)
dp = [0]*(N+1)
dp[1] = 1
ans = []
for i in range(1, N+1):
    a = len(graph[i])
    for j in graph[i]:
        dp[j] += float(dp[i])/a
    if not a:
        ans.append(i)
for i in ans:
    print(dp[i])