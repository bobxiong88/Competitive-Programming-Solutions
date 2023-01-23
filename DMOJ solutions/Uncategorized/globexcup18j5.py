import sys
from collections import deque
input = sys.stdin.readline
N, M, Q, C = map(int,input().split())
graph = {}
for i in range(1,N+1):
    graph.update({i:set()})
for i in range(M):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
dist = [float('inf')]*(N+1)
queue = deque([(C,0)])
dist[C] = 0
while queue:
    node, d = queue.popleft()
    if d>dist[node]:
        continue
    d+=1
    for n in graph[node]:
        if dist[n]>d:
            dist[n] = d
            queue.append((n,d))
for i in range(Q):
    a,b = map(int,input().split())
    ans = dist[a]+dist[b]
    print("This is a scam!" if ans==float('inf') else ans)