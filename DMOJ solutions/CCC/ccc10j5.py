def bfs(visited, graph, node, e):
  visited.append(node)
  
  queue=[(node,0)]

  depth = 0
  
  while queue:
   
    s,d = queue.pop(0)
    
    if d > depth:
        depth+=1
    
    if s == e:
        return depth
        
    
    try:
        for neighbour in graph[s]:
          
          if neighbour not in visited:
            visited.append(neighbour)
            queue.append((neighbour,depth+1))
    except:
        pass
            
graph = {}

A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

A = tuple(reversed(A))
B = tuple(reversed(B))

for y in range(1,9):
    for x in range(1,9):
        possible = []
        possible.append((y+2,x+1))
        possible.append((y+1,x+2))
        possible.append((y-1,x+2))
        possible.append((y-2,x+1))
        possible.append((y-2,x-1))
        possible.append((y-1,x-2))
        possible.append((y+1,x-2))
        possible.append((y+2,x-1))
        for p in possible:
            
            if p[0]<=0 or p[0]>=9 or p[1]<=0 or p[1]>=9:
                possible.remove(p)
        
        graph.update({(y,x):possible})

print(bfs([],graph,A,B))