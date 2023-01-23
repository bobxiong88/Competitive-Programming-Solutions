def board(grid):
    for row in grid:
        print("".join(row))
def bfs(grid, X, Y, start, end):
    queue = [(start, (0,0), 0)]
    dist = [[] for i in range(Y)]
    for i in range(Y):
        row = []
        for j in range(X):
            dist[i].append([])
        
    #print(dist)
    #dist[start[0]][start[1]].append((0,0))
    visited = [row.copy() for row in grid]
    while queue:
        node, v, d = queue.pop(0)
        i, j = node
        if grid[i][j] == "F":
            return str(d)
        visited[i][j] = "V"
        yv,xv = v
        vs = []
        if v!=(0,0):
            vs.append((yv,xv))
        vs.append((yv+1,xv))
        vs.append((yv,xv+1))
        vs.append((yv-1,xv))
        vs.append((yv,xv-1))
        vs.append((yv+1,xv+1))
        vs.append((yv+1,xv-1))
        vs.append((yv-1,xv+1))
        vs.append((yv-1,xv-1))
        #print(vs)
        for v in vs:
            yv,xv = v
            ny,nx = i+yv, j + xv
            if 0<= ny <Y and 0<= nx <X and -4<yv<4 and -4<xv<4:
                if (v in dist[ny][nx]) == False:
                    if (ny,nx) == end:
                        return str(d+1)
                    if grid[ny][nx] == " ":
                        dist[ny][nx].append(v)
                        queue.append(((ny,nx),(yv,xv),d+1))

    #board(visited)
    #print(dist[end[0]][end[1]])

    return False
                    
        


N = int(input())
for _ in range(N):
    X, Y = map(int,input().split())
    grid = [[" "]*X for i in range(Y)]
    x1,y1,x2,y2 = map(int,input().split())
    #grid[y1][x1] = "S"
    grid[y2][x2] = "F"
    P = int(input())
    for i in range(P):
        a,b,c,d = map(int,input().split())
        for i in range(Y):
            for j in range(X):
                if i in range(c,d+1) and j in range(a,b+1):
                    grid[i][j] = "#"
    #board(grid)
    ans = bfs(grid, X, Y, (y1,x1),(y2,x2))
    if not ans:
        print("No solution.")
    else:
        print("Optimal solution takes",ans,"hops.")