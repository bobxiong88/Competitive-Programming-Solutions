import sys
input = sys.stdin.readline
def p(board):
    for row in board:
        print(*row)
n,m = map(int,input().split())
grid = [list(input().strip('\n')) for i in range(n)]
up = [[0 for i in range(m)] for j in range(n)]
down = [[0 for i in range(m)] for j in range(n)]
left = [[0 for i in range(m)] for j in range(n)]
right = [[0 for i in range(m)] for j in range(n)]
for i in range(1,n):
    for j in range(m):
        if grid[i-1][j] == '*':
            up[i][j] = up[i-1][j]+1
for i in range(n-2, -1, -1):
    for j in range(m):
        if grid[i+1][j] == '*':
            down[i][j] = down[i+1][j]+1
for j in range(1,m):
    for i in range(n):
        if grid[i][j-1] == '*':
            left[i][j] = left[i][j-1]+1
for j in range(m-2, -1, -1):
    for i in range(n):
        if grid[i][j+1] == '*':
            right[i][j] = right[i][j+1]+1
stars = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            s = min(up[i][j], down[i][j], right[i][j], left[i][j])
            if s: stars.append((i,j,s))
new = [['.' for i in range(m)] for j in range(n)]
for x,y,s in stars:
    for i in range(-s,s+1):
        new[x+i][y] = '*'
        new[x][y+i] = '*'
if new == grid:
    print(len(stars))
    for i,j,x in stars:
        print(i+1,j+1,x)
else:
    print(-1)
