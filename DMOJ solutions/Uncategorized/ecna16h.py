def board(g):
    for row in g:
        print("".join(row[:-1]))
def fill(graph, r, c, i,j):
    graph[i][j] = "X"
    poss = []
    poss.append((i+1,j))
    poss.append((i,j+1))
    poss.append((i,j-1))
    poss.append((i-1,j))
    for p in poss:
        y,x = p
        if 0<=y<r and 0<=x<c:
            if graph[y][x] == ".":
                fill(graph, r, c, y, x)
def area(path, r,c):
    grid = [["."]*c for i in range(r)]
    for node in path:
        i, j = node
        grid[i][j] = "X"
    coords = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "X":
                a = 1
                grid[i+1][j+1] = "X"
                queue = [(i+1,j+1)]
                while queue:
                    node = queue.pop(0)
                    coords.append(node)
                    i, j = node
                    #board(grid)
                    poss = []
                    poss.append((i+1,j))
                    poss.append((i,j+1))
                    poss.append((i,j-1))
                    poss.append((i-1,j))
                    for p in poss:
                        y,x = p
                        if 0<=y<r and 0<=x<c:
                            if grid[y][x]==".":
                                grid[y][x] = "X"
                                a+=1
                                queue.append((y,x))  
                return coords
                
import sys
input = sys.stdin.readline
r,c = map(int,input().split())
graph = []
for i in range(r):
    graph.append(list(map(str,list(input()))))
A, B = False, False
inters = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == "A":
            A = (i,j)
        if graph[i][j] == "B":
            B = (i,j)
        if graph[i][j] == "X":
            try:
                if graph[i+1][j] == "X" and graph[i][j+1] == "X" and graph[i-1][j] == "X" and graph[i][j-1] == "X":
                    inters.append((i,j))
                    graph[i][j] = "I"
            except:
                pass


queue = [(A, [(-1,-1),A])]
Apaths = []
theA = [A]
while queue:
    node, path = queue.pop(0)
    i, j = node
    poss = []
    poss.append((i+1,j))
    poss.append((i,j+1))
    poss.append((i,j-1))
    poss.append((i-1,j))
    
    for p in poss:
        y, x = p
        if 0<=y<r and 0<=x<c:
            if len(path)>=2:
                if p==path[-2]:
                    continue
            if path[0] in inters and graph[y][x] == "X":
                queue.append((p,path+[p]))
            elif graph[y][x] == "X":
                queue.append((p,path+[p]))
                graph[y][x] = "A"
            
            if graph[y][x] == "I":
                if (inters[0] not in path) and (inters[1] not in path):
                    if theA == [A]:
                        theA = theA + path[2:]
                    else:
                        theA = list(reversed(path[2:])) + theA
                    queue.append((p, [p]))
                else:
                    Apaths.append(path+[p])
first = Apaths[0][0]
n = []
for i in Apaths:
    if i[0]== first:
        n.append(i)
Apaths = n[:]
# find the B paths ____________________________________________
# find the B paths ____________________________________________
# find the B paths ____________________________________________
queue = [(B, [(-1,-1),B])]
Bpaths = []
theB = [B]
while queue:
    node, path = queue.pop(0)
    i, j = node
    poss = []
    poss.append((i+1,j))
    poss.append((i,j+1))
    poss.append((i,j-1))
    poss.append((i-1,j))
    
    for p in poss:
        y, x = p
        if 0<=y<r and 0<=x<c:
            if len(path)>=2:
                if p==path[-2]:
                    continue
            if path[0] in inters and graph[y][x] == "X":
                queue.append((p,path+[p]))
            elif graph[y][x] == "X":
                queue.append((p,path+[p]))
                graph[y][x] = "B"
            
            if graph[y][x] == "I":
                if (inters[0] not in path) and (inters[1] not in path):
                    if theB == [B]:
                        theB = theB + path[2:]
                    else:
                        theB = list(reversed(path[2:])) + theB
                    queue.append((p, [p]))
                else:
                    Bpaths.append(path+[p])
first = Bpaths[0][0]
n = []
for i in Bpaths:
    if i[0]== first:
        n.append(i)
Bpaths = n[:]

for i in range(r):
    for j in range(c):
        if (i==0 or i==r-1 or j==0 or j==c-1) and graph[i][j] == ".":
            fill(graph, r, c, i ,j)

Aone = theA + Bpaths[0]
Bone = theB + Bpaths[1]

for node in Aone:
    i,j = node
    if node not in inters:
        graph[i][j] = "A"
for node in Bone:
    i,j = node
    if node not in inters:
        graph[i][j] = "B"
i,j = inters[0]

if graph[i+1][j] == graph[i-1][j]:
    pass
    #print("correct")
else:
    #print("incorrect")
    Aone = theA + Bpaths[1]
    Bone = theB + Bpaths[0]
    for node in Aone:
        i,j = node
        if node not in inters:
            graph[i][j] = "A"
    for node in Bone:
        i,j = node
        if node not in inters:
            graph[i][j] = "B"
Acoords = area(Aone, r, c)
Bcoords = area(Bone, r, c)
for coord in Acoords:
    i, j = coord
    graph[i][j] = "a"
for coord in Bcoords:
    i, j = coord
    if graph[i][j]== ".":
        graph[i][j]="b"
    elif graph[i][j]=="a":
        graph[i][j] = "o"
for coord in Bone:
    i,j = coord
    if coord in inters:
        pass
    else:
        graph[i][j] = "B"
a,b,o = 0,0,0
for i in range(r):
    for j in range(c):
        if graph[i][j]=="a":
            a+=1
        if graph[i][j]=="b":
            b+=1
        if graph[i][j]=="o":
            o+=1
print(a,b,o)