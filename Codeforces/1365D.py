import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    grid = []
    bad = []
    good = 0
    for i in range(n):
        line = list(input())
        for j in range(m):
            if line[j]=='G':
                good+=1
            elif line[j] =='B':
                bad.append((i,j))
        grid.append(line)
    for i,j in bad:
        pos = [(0,1),(0,-1),(1,0),(-1,0)]
        for a,b in pos:
            x,y = i+a,j+b
            if 0<=x<n and 0<=y<m:
                grid[x][y] = '#'
    queue = deque([(n-1,m-1)])
    if not good:
        print("Yes")
        continue
    if grid[n-1][m-1] == '#':
        print("No")
        continue
    while queue:
        i,j = queue.popleft()
        pos = [(0,1),(0,-1),(1,0),(-1,0)]
        for a,b in pos:
            x,y = i+a, j+b
            if 0<=x<n and 0<=y<m:
                if grid[x][y]!='#':
                    if grid[x][y]=='G':
                        good-=1
                    grid[x][y] = '#'
                    queue.append((x,y))
    if not good:
        print("Yes")
    else:
        print("No")
                    
