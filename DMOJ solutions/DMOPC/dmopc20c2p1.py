import sys
input = sys.stdin.readline
N = int(input())
s = input().strip('\n')
grid = [['.' for i in range(1005)] for j in range(1005)]
x,y = 0,0
minx,miny = float('inf'),float('inf')
mx,my = 0,0
for i in s:
    if i == '^':
        grid[x][y] = '/'
        minx = min(minx, x)
        miny = min(miny, y)
        mx = max(mx, x)
        my = max(my, y)
        y += 1
        x -=1
    elif i == 'v':
        x += 1
        grid[x][y] = '\\'
        minx = min(minx, x)
        miny = min(miny, y)
        mx = max(mx, x)
        my = max(my,y)
        y += 1
    else:
        grid[x][y] = '_'
        minx = min(minx, x)
        miny = min(miny, y)
        mx = max(mx, x)
        my = max(my,y)
        y += 1
for i in range(minx,mx+1):
    print(''.join(grid[i][miny:my+1]))