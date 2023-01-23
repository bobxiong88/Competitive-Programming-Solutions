def bfs(graph,vertices,visited,vertex):
    queue = [vertex]
    visited[vertex] = True
    colors = set()
    while queue:
        node = queue.pop(0)
        try:
            color = vertices[node].pop(0)
        except:
            return False
        colors.update({color})
        try:
        
            for n in graph[node]:
                
                if color in vertices[n]:
                    vertices[n].remove(color)
                    if visited[n]==False:
                        queue.append(n)
                        visited[n]=True
        except:
            pass

                
    return len(colors)
    
    
    
for _ in range(5):
    
    graph = {}
    N = int(input())
    visited = [False]*(N+1)
    vertices = [[]]
    for p in range(N):
        a,b = [int(i) for i in input().split()]
        if a in graph.keys():
            graph[a].append(b)
        else:
            graph.update({a:[b]})
        if b in graph.keys():
            graph[b].append(a)
        else:
            graph.update({b:[a]})
        

                
        vertices.append([1,2,3,4])
    real = -1
    while True:
        find = False
        for p,i in enumerate(vertices):
            if len(i)==4:
                find = True
                break
        if find==False:
            break
        
        val = bfs(graph, vertices, visited, p)
        if val == False:
            print(0)
            break
        real = max(val,real)
    if real!=-1:
        print(real)