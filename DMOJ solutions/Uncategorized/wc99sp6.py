import sys
from heapq import *
input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int,input().split())
    grid = [list(map(int,input().split())) for i in range(N)]
    vis = [[False for i in range(M)] for j in range(N)]
    ans = 0
    queue = []
    heapify(queue)
    for i in range(N):
        for j in range(M):
            if not i or not j or i==N-1 or j == M-1:
                heappush(queue, (grid[i][j], (i,j)))
                vis[i][j] = True
    while queue:
        v, p = heappop(queue)
        i, j = p
        ans += v-grid[i][j]
        for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
            x += i
            y += j
            if x not in range(N) or y not in range(M): continue
            if vis[x][y]: continue
            vis[x][y] = True
            heappush(queue, (max(grid[x][y], v),(x,y)))
    print(ans)