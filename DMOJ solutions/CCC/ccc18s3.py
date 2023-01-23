def bfs(graph,robot,N,M):
    distGraph = [[float('inf')]*M for i in range(N)]

    queue = [robot]

    distGraph[robot[0]][robot[1]]=0
    if graph[robot[0]][robot[1]]=="*":
        return distGraph
    while queue:
        y,x = queue.pop(0)
        
        distance = distGraph[y][x]
        
        if graph[y][x]=="." or graph[y][x]=="S":
            possible = []
            possible.append((y+1,x))
            possible.append((y,x+1))
            possible.append((y-1,x))
            possible.append((y,x-1))
            for p in possible:
                if graph[p[0]][p[1]]!="W" and graph[p[0]][p[1]]!="*" and graph[p[0]][p[1]]!="C":
                
                    if distance+1<distGraph[p[0]][p[1]]:
                        queue.append(p)
                        
                        distGraph[p[0]][p[1]] = distance+1
        else:
            
            if graph[y][x]=="L":
                n = (y,x-1)
            elif graph[y][x]=="R":
                n = (y,x+1)
            elif graph[y][x]=="U":
                n = (y-1,x)
            elif graph[y][x]=="D":
                n = (y+1,x)
            
            if graph[n[0]][n[1]]!="W" and graph[n[0]][n[1]]!="C" and graph[n[0]][n[1]]!="*":
                if distGraph[n[0]][n[1]]>distance or distGraph[n[0]][n[1]]==float('inf'):
                    distGraph[n[0]][n[1]]=distance
                    queue.append(n)
    return distGraph
N, M = map(int,input().split())
graph = []
robot = 0
for r in range(N):
    row = list(input())
    graph.append(row)
    if not robot:
        try:
            robot = (r,row.index("S"))
        except:
            pass
for r in range(N):
    for c in range(M):
        if graph[r][c] == "C":
            possible = []
            for i in range(c,0,-1):
                if graph[r][i]=="W":
                    break
                if graph[r][i]=="." or graph[r][i]=="S":
                    graph[r][i]="*"
            for i in range(c,M):
                if graph[r][i]=="W":
                    break
                if graph[r][i]=="."or graph[r][i]=="S":
                    graph[r][i]="*"

            
            for i in range(r,0,-1):
                if graph[i][c]=="W":
                    break
                if graph[i][c]=="."or graph[i][c]=="S":
                    graph[i][c]="*"
                    
            for i in range(r,N):
                if graph[i][c]=="W":
                    break
                if graph[i][c]=="."or graph[i][c]=="S":
                    graph[i][c]="*"
                    
distGraph = bfs(graph,robot,N,M)
graph[robot[0]][robot[1]]="S"
for r in range(N):
    for c in range(M):
        if graph[r][c]=="." or graph[r][c]=="*":
            val = distGraph[r][c]
            if val==float('inf'):
                val = -1
            print(val)