import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]
dist = [[0 for i in range(j)] for j in range(1,N+1)]
dist[0][0] = grid[0][0]
queue = deque([(0,0)])
while queue:
    i,j = queue.popleft()
    if i == N-1:
        continue
    for x,y in [(i+1, j),(i+1,j+1)]:
        if y>x: continue
        if dist[x][y] < dist[i][j]+grid[x][y]:
            dist[x][y] = dist[i][j]+grid[x][y]
            queue.append((x,y))
print(max(dist[-1]))