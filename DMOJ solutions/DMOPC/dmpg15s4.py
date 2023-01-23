def bfs(graph,a,b):
    visited = list(graph.keys())

    queue = [a]

    visited.remove(a)

    while queue:

        node = queue.pop(0)

        x,y,r = graph[node]
        
        if node == b:
            return True
        c=0
        for point in visited:
            if ((x-graph[point][0])**2+(y-graph[point][1])**2)**0.5<=r:
                c+=1
                if c>10:
                    break
                queue.append(point)
                if point==b:
                    return True
                visited.remove(point)
            
    return False



B, Q = [int(i) for i in input().split()]
graph = {}
for a in range(B):
    x,y,r = [int(i) for i in input().split()]
    graph.update({a+1:(x,y,r)})

for q in range(Q):
    a,b = [int(i) for i in input().split()]
    if bfs(graph,a,b)==True:
        print("YES")
    else:
        print("NO")