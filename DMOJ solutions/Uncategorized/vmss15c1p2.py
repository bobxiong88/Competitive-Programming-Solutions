import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int,input().split())
grid = []
for i in range(r):
    grid.append(list(input()))
visited = [[False]*c for i in range(r)]
t = 0
for i in range(r):
    for j in range(c):
        if grid[i][j]!="X":
            t+=1
            queue = deque([(i, j)])
            grid[i][j] = "X"
            while queue:
                x,y = queue.popleft()
                pos = [(x+1,y), (x, y+1), (x-1, y), (x, y-1)]
                for n in pos:
                    a, b = n
                    if 0<=a<r and 0<=b<c:
                        if grid[a][b]!="X":
                            queue.append((a,b))
                            grid[a][b] = "X"
print(t)