def printGraph(graph):
    for row in graph:
        print("".join(row))
def bfs(graph, S, floods):

    queue = [(S,0)]
    R,C = len(graph),len(graph[0])
    distance = [[2502]*C for i in range(R)]
    depth = 0
    distance[S[0]][S[1]] = 0
    graph[S[0]][S[1]] = "."
    while queue:
        
        node,d = queue.pop(0)
        
        if d>depth:
            
            depth+=1
            newFloods = []
            for flood in floods:
             
                wetLands = []
                wetLands.append((flood[0]+1,flood[1]))
                wetLands.append((flood[0],flood[1]+1))
                wetLands.append((flood[0]-1,flood[1]))
                wetLands.append((flood[0],flood[1]-1))
                for wetLand in wetLands:
                    if 0<=wetLand[0]<R and 0<=wetLand[1]<C:
                        if graph[wetLand[0]][wetLand[1]]==".":
                            graph[wetLand[0]][wetLand[1]]="*"
                            newFloods.append((wetLand[0],wetLand[1]))
                
            floods = newFloods
            
        
        if graph[node[0]][node[1]] == "D":
            return distance[node[0]][node[1]]
        
        currentDistance = distance[node[0]][node[1]]
        fields = []
        fields.append((node[0]+1,node[1]))
        fields.append((node[0],node[1]+1))
        fields.append((node[0]-1,node[1]))
        fields.append((node[0],node[1]-1))
        if graph[node[0]][node[1]]!= "*":
                
            for field in fields:
                y,x = field
                if 0<=y<R and 0<=x<C:
                    if graph[y][x]!="X" and graph[y][x]!="*":
                        if currentDistance+1<distance[y][x]:
                            distance[y][x] = currentDistance+1
                            queue.append(((y,x),depth+1))
                            if graph[node[0]][node[1]] == "D":
                                return distance[node[0]][node[1]]
    return False
R,C = [int(i) for i in input().split()]
graph = []
S = 0
floods = []
for i in range(R):
    row = list(input())
    graph.append(row)
    
    for j in range(C):
        if row[j] == "*":
            floods.append((i,j))
        elif row[j] == "S":
            S = (i,j)

val   = bfs(graph, S, floods)
print("KAKTUS" if not val else val)