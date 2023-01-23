import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph  = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
distOne = [0]*(N+1)
distTwo = [0]*(N+1)
queue = deque([(1,1,-1)])
far, df = 1, 1
while queue:
    node, d, p = queue.popleft()
    if d>df:
        far = node
        df = d
    for n in graph[node]:
        if n!=p:
            queue.append((n,d+1,node))
distOne[far] = 1
queue = deque([(far, 1, -1)])
df = 1
while queue:
    node, d, p = queue.popleft()
    if d>df:
        far = node
        df = d
    for n in graph[node]:
        if n!=p:
            queue.append((n,d+1,node))
            distOne[n] = d+1
distTwo[far] = 1
queue = deque([(far, 1, -1)])
while queue:
    node, d, p = queue.popleft()
    for n in graph[node]:
        if n!=p:
            queue.append((n,d+1,node))
            distTwo[n] = d+1
for i in range(1, N+1):
    print(max(distOne[i], distTwo[i]))