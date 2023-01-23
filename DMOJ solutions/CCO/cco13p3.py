import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
parent = [0 for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
far, d = 1, 0
queue = deque([(1,0,-1)])
while queue:
    node, dist, p = queue.popleft()
    if dist > d:
        far,d = node, dist
    for n in graph[node]:
        if n!=p:
            queue.append((n, dist+1, node))
start = far
queue = deque([(far, 0, -1)])
d = 0
while queue:
    node, dist, p = queue.popleft()
    if dist > d:
        far, d = node, dist
    for n in graph[node]:
        if n!=p:
            queue.append((n, dist+1, node))
            parent[n] = node
diameter = [far]
queue = deque([far])
while queue:
    node = queue.popleft()
    diameter.append(parent[node])
    if parent[node] == start:
        break
    queue.append(parent[node])
index = len(diameter)//2-((len(diameter)%2)^1)
center = diameter[index]
queue = deque([])
paths = [0]*len(graph[center])
c = 0
for node in graph[center]:
    queue.append((node, 1, center, c))
    c+=1
if len(diameter)%2==0:
    while queue:
        node, d, p, c = queue.popleft()
        if d==index+1:
            long = c
            break
        for n in graph[node]:
            if n!=p:
                queue.append((n, d+1, node, c))
    queue = deque([])
    nLong = 0
    c=0
    for node in graph[center]:
        queue.append((node, 1, center, c))
        c+=1
    while queue:
        node, d, p, c = queue.popleft()
        if d==index and c!=long:
            paths[c]+=1
        if d==index+1:
            nLong+=1
        for n in graph[node]:
            if n!=p:
                queue.append((n, d+1, node, c))
    s = 0
    for path in paths:
        s+=nLong*path
else:
    while queue:
        node, d, p, c = queue.popleft()
        if d==index:
            paths[c]+=1
        for n in graph[node]:
            if n!=p:
                queue.append((n, d+1, node, c))
    s = 0
    suffix = [0]*len(paths)
    for i in range(1,len(paths)+1):
        s += paths[-i]
        suffix[-i] = s
    s = 0
    for i in range(len(paths)-1):
        s+=paths[i]*suffix[i+1]
print(len(diameter), s)