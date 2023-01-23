from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
grid = []
for i in range(n):
    grid.append(list(input()))
start = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == "s":
            start = (i, j)
            break
    if start:
        break
visited = [[float('inf')]*m for i in range(n)]
visited[start[0]][start[1]] = 0
queue = deque([start])
ans = -1
while queue:
    y,x = queue.popleft()
    if grid[y][x]=="e":
        ans = visited[y][x]
        break
    pos = []
    pos.append((y+1,x))
    pos.append((y,x+1))
    pos.append((y-1,x))
    pos.append((y,x-1))
    for p in pos:
        i, j = p
        if 0<=i<n and 0<=j<m:
            if grid[i][j]!="X":
                if visited[i][j]>visited[y][x]+1:
                    visited[i][j] = visited[y][x]+1
                    queue.append((p))
if ans!=-1:
    print(ans-1)
else:
    print(ans)