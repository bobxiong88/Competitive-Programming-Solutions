import sys
from collections import deque
input = sys.stdin.readline
def find_sub(graph,start,N,locations):
    de = deque([(start,-1)])
    newGraph = [False]*N
    g = {}
    newGraph[start] = True
    while de:
        node,p = de.popleft()
        if locations[node] == True:
            newGraph[node] = True
            q = deque([node])
            while q:
                a = q.popleft()
                if a==start:
                    break
                newGraph[g[a]]=True
                if locations[g[a]]==True:
                    break
                q.append(g[a])

        for n in graph[node]:
            if n!=p:
                g[n] = node
                de.append((n,node))
    return newGraph
def bfs(graph,node, N, locations):
    queue = deque([(node,0,-1)])
    depth = 0
    while queue:
        node,d,p = queue.popleft()
        if d>depth:
            depth+=1
        for n in graph[node]:
            if n!=p and locations[n]==True:
                queue.append((n,depth+1,node))
    return node,depth
N, M = map(int,input().split())
points = list(map(int,input().split()))
graph = {}
for i in range(N-1):
    a,b = map(int,input().split())
    try:
        graph[a].append(b)
    except:
        graph.update({a:[b]})
    try:
        graph[b].append(a)
    except:
        graph.update({b:[a]})
    
locations = [False]*N
for i in points:
    locations[i] = True
p = points[0]
locations = find_sub(graph,p,N,locations)
n = points[0]
node, depth = bfs(graph,n,N,locations)
node, diameter = bfs(graph,node,N,locations)
c=0
for i in locations:
    if i==True:
        c+=1
print((c-1)*2-diameter)