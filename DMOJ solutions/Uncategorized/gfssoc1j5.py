import sys
from collections import deque
input = sys.stdin.readline
N, M, T = map(int,input().split())
g = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    g[a].append(b)
ans = [[]]
for i in range(1, N+1):
    dist = [float('inf')]*(N+1)
    dist[i] = 0
    queue = deque([(i, 0)])
    while queue:
        node, d = queue.popleft()
        if d>dist[node]:
            continue
        for n in g[node]:
            if dist[n] > d + T:
                dist[n] = d + T
                queue.append((n,d+T))
    ans.append(dist)
Q = int(input())
for i in range(Q):
    a,b = map(int,input().split())
    d = ans[a][b]
    if d==float('inf'): d = "Not enough hallways!"
    print(d)