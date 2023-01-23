import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
grid = [list(input()) for i in range(N)]
dist = [[0]*N for i in range(N)]
dist[0][0] = 1
queue = deque([(0,0,0,0,0)])
while queue:
    x,y,a,b,c = queue.popleft()
    if (x,y) == (N-1,N-1): break
    aa, bb, cc = a, b, c
    for i,j in (x+1,y),(x,y+1),(x,y-1):
        if 0<=i<N and 0<=j<N:
            if grid[i][j]=='.':
                if not dist[i][j]:
                    if i == x+1: a+=1
                    elif j == y+1: b+=1
                    else: c+=1
                    dist[i][j] = 1
                    queue.append((i,j,a,b,c))
        a, b, c = aa, bb, cc
ans = a**2+b**2+c**2
print(-1 if not dist[-1][-1] else ans)