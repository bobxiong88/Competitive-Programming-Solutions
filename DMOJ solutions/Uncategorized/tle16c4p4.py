import sys
from collections import deque
def bfs(start):
    queue = deque([start])
    dist[start] = 0
    far, d = start, 0
    nodes = [start]
    while queue:
        node = queue.popleft()
        if dist[node] > d:
            far, d = node, dist[node]
        for n in graph[node]:
            if graph[node][n] + dist[node] < dist[n]:
                dist[n] = graph[node][n] + dist[node]
                queue.append(n)
                nodes.append(n)
    for n in nodes:
        visited[n] = True
        dist[n] = float('inf')
    return far, d
input = sys.stdin.readline
N, M, Q = map(int,input().split())
graph = []
for i in range(N+1):
    graph.append({})
for i in range(M):
    u,v,l = map(int,input().split())
    graph[u].update({v:l})
    graph[v].update({u:l})
if Q==1:
    dias = []
    dist = [float('inf')]*(N+1)
    visited = [False]*(N+1)
    for node in range(1, N+1):
        if not visited[node]:
            node, _ = bfs(node)
            node, d = bfs(node)
            dias.append(d)
    print(sum(dias)+len(dias)-1)
else:
    radi = []
    dist = [float('inf')]*(N+1)
    visited = [False]*(N+1)
    roots = [0 for i in range(N+1)]
    
    for node in range(1,N+1):
        if not visited[node]:
            start, _ = bfs(node)
            queue = deque([start])
            dist[start] = 0
            far, d = start, 0
            nodes = [start]
            while queue:
                node = queue.popleft()
                if dist[node] > d:
                    far, d = node, dist[node]
                for n in graph[node]:
                    if graph[node][n] + dist[node] < dist[n]:
                        dist[n] = graph[node][n] + dist[node]
                        queue.append(n)
                        nodes.append(n)
                        roots[n]=node
            for n in nodes:
                visited[n] = True
                dist[n] = float('inf')
            edges = []
            queue = deque([far])
            while queue:
                node = queue.popleft()
                if node==start:
                    break
                queue.append(roots[node])
                edges.append(graph[node][roots[node]])
            left, right = sum(edges), 0
            diff, radius = float('inf'), 0
            for i in range(len(edges)):
                left -= edges[i]
                right += edges[i]
                if abs(left-right)<diff:
                    radius = max(left, right)
                    diff = abs(left-right)
                if abs(left-right)==diff:
                    radius = max(radius, left, right)
            radi.append(radius)
    radius = max(radi)
    radi.remove(radius)
    if radius in radi:
        radius+=1
    print(radius)