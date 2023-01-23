def bfs(graph, N, M, node, level):
    queue = [node]
    visited = [node]
   
    while queue:
        y,x = queue.pop(0)
        
        if y==0 or x==0 or y==N-1 or x==M-1:
            return False
        p = []
        p.append((y-1,x))
        p.append((y,x-1))
        p.append((y+1,x))
        p.append((y,x+1))
        for i in p:
            if i not in visited:
                if graph[i[0]][i[1]]<level:
                    visited.append(i)
                    queue.append((i[0],i[1]))
    return True
    
for _ in range(5):
    N, M = map(int,raw_input().split())
    world = []
    waterworld = []
    for i in range(N):
        row = list(map(int,raw_input().split()))
        world.append(row)
        waterworld.append(row)
    total = 0
    
    for i in range(1,51):
        for y in range(1,N-1):
            for x in range(1,M-1):
                c = waterworld[y][x]
                if c<i:
                    if bfs(world,N,M,(y,x),c+1):
                        total+=1
                        waterworld[y][x]+=1
    print(total)
    if _>=4:
        break