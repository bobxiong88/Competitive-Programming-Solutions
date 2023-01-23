import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph = {}
for i in range(1,N+1):
    graph.update({i:[]})
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(N+1)
c = 0
for i in range(1,N+1):
    if not visited[i]:
        c+=1
        visited[i] = True
        queue = deque([i])
        while queue:
            node = queue.popleft()
            for n in graph[node]:
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)
if M == N-c or M == N-c+1:
    print("YES")
else:
    print("NO")