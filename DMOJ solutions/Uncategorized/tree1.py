from collections import deque
import sys
input = sys.stdin.readline
n = 4
c = 0
graph = [[] for i in range(n)]
for i in range(n):
    line = list(map(int,input().split()))
    for j in range(i+1,n):
        if line[j]:
            graph[i].append(j)
            graph[j].append(i)
            c+=1
vis = [False for i in range(n)]
vis[0] = True
queue = deque([0])
while queue:
    node = queue.popleft()
    for v in graph[node]:
        if not vis[v]:
            vis[v] = True
            queue.append(v)
if all(vis) and c==n-1:
    print("Yes")
else:
    print("No")