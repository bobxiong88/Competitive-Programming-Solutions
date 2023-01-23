# construct graph
# bfs while keeping in track of exposure and distance
# find all the path <=exposure
# find path with least distance
# V:{V1:[d,u],V2:[d,u],V3:[d,u]}
# queue = [(N, visited, sun, distance)]
def bfs(graph, N, S):
    visited = [0]
    queue = [(0, visited, 0, 0)]
    dist = float('inf')
    while queue:
        
        node, visited, sun, distance = queue.pop(0)
        if sun>S:
            pass
        elif node == N-1:
            if distance<dist:
                dist = distance
        elif distance>=dist:
            pass
        else:
            for i in graph[node].keys():
                if i not in visited:
                    
                    
                    if graph[node][i][1]==1:
                        queue.append((i,visited+[i],sun+graph[node][i][0],distance+graph[node][i][0]))
                    else:
                        queue.append((i,visited+[i],sun,distance+graph[node][i][0]))
    if dist == float('inf'):
        print (-1)
    else:
        print (dist)
            
S = int(input())

N,E = map(int,input().split())

graph = {}

for i in range(N):
    graph.update({i:{}})

for i in range(E):
    s,t,d,u = map(int,input().split())
    graph[s].update({t:[d,u]})
    graph[t].update({s:[d,u]})

bfs(graph,N,S)