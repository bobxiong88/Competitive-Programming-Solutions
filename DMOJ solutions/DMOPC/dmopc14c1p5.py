R, C = map(int,input().split())
start = tuple(map(int,input().split()))
end = tuple(map(int,input().split()))
grid = []
for i in range(R):
    grid.append(list(input()))

T = int(input())
devices = []
for i in range(T):
    y,x = map(int,input().split())
    grid[y][x] = "T"

queue = [start]
dist = [[float('inf')]*(C) for i in range(R)]
dist[start[0]][start[1]]=0
minDis = float('inf')
while queue:
    node = queue.pop(0)
    y,x = node
    d = dist[y][x]
    if grid[y][x]=="T":
        minDis = min(minDis,d)
    ps = []
    ps.append((y+1,x))
    ps.append((y,x+1))
    ps.append((y-1,x))
    ps.append((y,x-1))
    for p in ps:
        if 0<=p[0]<R and 0<=p[1]<C:
            if grid[p[0]][p[1]]!="X":
                if d+1<dist[p[0]][p[1]]:
                    dist[p[0]][p[1]] = d+1
                    queue.append(p)
print(max(0,dist[end[0]][end[1]]-minDis))