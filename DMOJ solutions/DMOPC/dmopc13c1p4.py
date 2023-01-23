def findPoo(graph,comp,R,C):
    distGraph = [[100000]*C for i in range(R)]
    distGraph[comp[0]][comp[1]] = 0
    queue = [comp]
    while queue:
        y,x = queue.pop(0)
        distance = distGraph[y][x]
        possible = []
        possible.append((y+1,x))
        possible.append((y,x+1))
        possible.append((y-1,x))
        possible.append((y,x-1))
        for p in possible:
            r,c = p
            if 0<=r<R and 0<=c<C:
                if distance+1<distGraph[r][c] and graph[r][c]!="X":
                    distGraph[r][c] = distance + 1
                    queue.append((r,c))
                    if distance+1 >= 60:
                        return False
                    if graph[r][c]=="W":
                        return distance+1

    return False
                    
T = int(input())

for _ in range(T):
    l,w = [int(i) for i in raw_input().split()]
    comp = 0
    graph = []
    for r in range(w):
        row = list(raw_input())
        if comp==0:
            try:
                comp = (r,row.index("C"))
            except:
                pass
        graph.append(list(row))
    val = findPoo(graph,comp,w,l)
    if val==False:
        print("#notworth")
    else:
        print(val)