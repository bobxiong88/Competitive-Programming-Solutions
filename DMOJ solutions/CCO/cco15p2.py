import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N)]
dp = [[0]*(2**N) for j in range(N)]
for i in range(M):
    s, d, l = map(int,input().split())
    graph[s].append((d,l))
for vis in range(2**N):
    for node in range(N):
        if (vis >> node)&1: continue
        if dp[node][vis] == 0 and node != 0: continue
        for n, w in graph[node]:
            if (vis >> n)&1: continue
            dp[n][vis|(1<<node)] = max(dp[node][vis]+w, dp[n][vis|(1<<node)])
print(max(dp[N-1]))