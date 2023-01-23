from collections import deque
import sys
input = sys.stdin.readline
V, E = int(input()), int(input())
graph = {}
for i in range(1,V+1):
    graph.update({i:{}})
for i in range(E):
    m, n, d, s = map(float,input().split())
    weight = float(d)/float(s)*60
    try:
        if graph[m][n] > weight:
            graph[m][n] = weight
    except:
        graph[m].update({n:weight})
    try:
        if graph[n][m] > weight:
            graph[n][m] = weight
    except:
        graph[n].update({m:weight})
queue = deque([(1,0,0)])
dist = [[float('inf'),float('inf')] for i in range(V+1)]
dist[1] = [0,0]
while queue:
    node, d, time = queue.popleft()
    d+=1
    if time>dist[node][0]:
        continue
    for n in graph[node]:
        n = int(n)
        peepee = time + graph[node][n]
        if dist[n][0] > peepee:
            dist[n][0] = peepee
            dist[n][1] = d
            queue.append((n, d, peepee))
print(dist[V][1])
print(int(round(dist[V][0]/3)))