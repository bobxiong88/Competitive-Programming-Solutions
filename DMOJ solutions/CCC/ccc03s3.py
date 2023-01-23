def flood_fill(graph, x, y, n):
    n.append(0)
    graph[y][x]="I"
    
    if y-1>=0:
        if graph[y-1][x]==".":
            
            flood_fill(graph, x, y-1, n)
    

    if y+1<=len(graph)-1:
        if graph[y+1][x]==".":
            
            flood_fill(graph, x, y+1, n)
 

    if x-1>=0:
        if graph[y][x-1]==".":
            
            flood_fill(graph, x-1, y, n)
   
    if x+1<=len(graph[0])-1:
        if graph[y][x+1]==".":
            
            flood_fill(graph, x+1, y, n)
    
    
    return len(n)

tiles = int(input())
rowNum = int(input())
columnNum = int(input())

graph = []

for i in range(rowNum):
    row = list(input())
    graph.append(row)

    


roomSize = []


    
for yp, row in enumerate(graph):
    
    if "." in row:
        
        xp = row.index(".")
        
        roomSize.append(flood_fill(graph,xp,yp,[]))

roomSize = sorted(roomSize)
roomSize = list(reversed(roomSize))
for i,room in enumerate(roomSize):
    tiles-=room
    if tiles<=0:
        break
roomstr = "rooms,"

    
if tiles<0:
    if i==1:
        roomstr = "room,"
    print(i,roomstr,roomSize[i]+tiles,"square metre(s) left over")
else:
    if len(roomSize)==1:
        roomstr ="room,"
    print(len(roomSize),roomstr,tiles,"square metre(s) left over")