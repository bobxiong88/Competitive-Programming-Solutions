import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for i in range(t):
    r = int(input())
    c = int(input())
    grid = []
    for i in range(r):
        grid.append(list(input()))
    dist = [[float('inf')]*c for i in range(r)]
    dist[0][0] = 1
    queue = deque([(0,0)])
    while queue:
        y,x = queue.popleft()
        if (y,x) == (r-1,c-1):
            break
        pos = []
        if grid[y][x]=="+":
            pos.append((y+1,x))
            pos.append((y,x+1))
            pos.append((y-1,x))
            pos.append((y,x-1))
        elif grid[y][x]=="-":
            pos.append((y,x+1))
            pos.append((y,x-1))
        elif grid[y][x]=="|":
            pos.append((y+1,x))
            pos.append((y-1,x))
        
        for p in pos:
            i, j = p
            if 0<=i<r and 0<=j<c and grid[i][j]!="*":
                if dist[i][j]>dist[y][x]+1:
                    dist[i][j] = dist[y][x]+1
                    queue.append((i,j))
    ans = dist[r-1][c-1]
    if ans==float('inf'):
        ans = -1
    print(ans)