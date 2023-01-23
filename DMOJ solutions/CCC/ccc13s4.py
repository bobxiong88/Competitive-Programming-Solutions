def dfs(visited, graph, node, end):
    if visited[node] != True:
        visited[node] = True
        if node==end:
            return visited
        for n in graph[node]:    
            dfs(visited, graph, n, end)
    return visited

graph = {}

N, M = [int(i) for i in raw_input().split()]

for i in range(N):
    graph.update({i:[]})

for i in range(M):
    x, y = [int(i) for i in raw_input().split()]
    
    graph[x-1].append(y-1)

p, q = [int(i)-1 for i in raw_input().split()]

pFind = dfs([False for i in range(N)],graph,p,q)[q]
qFind = dfs([False for i in range(N)],graph,q,p)[p]

if pFind == qFind:
    print("unknown")
elif pFind == False:
    print("no")
elif qFind == False:
    print("yes")
else:
    print("unknown")