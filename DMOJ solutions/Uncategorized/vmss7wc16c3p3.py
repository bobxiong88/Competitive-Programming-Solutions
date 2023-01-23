import sys
from collections import deque
input = sys.stdin.readline
N, M, B, Q = map(int,input().split())
graph = {}
for i in range(1,N+1):
    graph.update({i:{}})
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].update({b:c})
    graph[b].update({a:c})
queue = deque([B])
dist = [float('inf')]*(N+1)
dist[B] = 0
while queue:
    node = queue.popleft()
    for n in graph[node]:
        if dist[n] > dist[node] + graph[node][n]:
            dist[n] = dist[node] + graph[node][n]
            queue.append(n)
for i in range(Q):
    ans = dist[int(input())]
    if ans==float('inf'):
        ans = -1
    print(ans)