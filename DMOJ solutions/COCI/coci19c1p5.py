def bfs(graph,R,C):

    
    color = graph[R-1][C-1]
    visited = [[False]*C for i in range(R)]
    visited[R-1][C-1] = True
    queue = [(R-1,C-1)]
    secondQueue = []
    depth = 0
    while queue!=[] or secondQueue!=[]:
        color = graph[R-1][C-1]
        while queue!=[]:
            y,x = queue.pop(0)
            

            
            possible = []
            possible.append((y+1,x))
            possible.append((y,x+1))
            possible.append((y-1,x))
            possible.append((y,x-1))
            
            for p in possible:
                if 0<=p[0]<R and 0<=p[1]<C and visited[p[0]][p[1]]==False and graph[p[0]][p[1]]!="*":
                    
                    if graph[p[0]][p[1]]==color:
                        queue.append(p)

                    elif graph[p[0]][p[1]]!=color:
                        
                        secondQueue.append(p)
                    
                    visited[p[0]][p[1]]=True
        depth+=1
        if queue==[] and secondQueue==[]:
            break
        
        color = graph[secondQueue[0][0]][secondQueue[0][1]]
        
        while secondQueue:
            coord = secondQueue.pop(0)
            
            y,x = coord
            visited[y][x]=True
            possible = []
            possible.append((y+1,x))
            possible.append((y,x+1))
            possible.append((y-1,x))
            possible.append((y,x-1))
            for p in possible:
                if 0<=p[0]<R and 0<=p[1]<C and visited[p[0]][p[1]]==False and graph[p[0]][p[1]]!="*":
                    
                    if graph[p[0]][p[1]]==color:
                        secondQueue.append(p)
                    elif graph[p[0]][p[1]]!=color:

                        queue.append(p)
                    
                    visited[p[0]][p[1]]=True
        
        depth+=1
    return depth



                

R, C = [int(i) for i in input().split()]

graph = []

tracks = []
for r in range(R):
    row = list(input())
    graph.append(row)



print(bfs(graph, R,C))