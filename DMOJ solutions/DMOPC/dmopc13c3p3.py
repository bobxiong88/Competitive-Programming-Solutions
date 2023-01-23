from collections import deque
import sys
input = sys.stdin.readline
grid = []
N, H = map(int,input().split())
for i in range(N):
    grid.append(list(map(int,input().split())))
visited = [[False]*N for i in range(N)]
visited[0][0] = True
queue = deque([(0,0)])
found = False
while queue:
    y,x = queue.popleft()
    h = grid[y][x]
    if (y,x) == (N-1,N-1):
        found = True
        break
    pos = []
    pos.append([y+1,x])
    pos.append([y-1,x])
    pos.append([y,x+1])
    pos.append([y,x-1])
    for p in pos:
        i, j = p
        if 0<=i<N and 0<=j<N:
            if abs(h-grid[i][j])<=H and visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True
            
if found:
    print("yes")
else:
    print("no")