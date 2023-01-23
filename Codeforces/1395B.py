import sys
input = sys.stdin.readline
n, m, x, y = map(int,input().split())
grid = [[0]*(m+1) for i in range(n+1)]
c = 1
for i in range(x, n+1):
    print(i, y)
    grid[i][y] = c
    c+=1
for i in range(x-1, 0, -1):
    print(i, y)
    grid[i][y] = c
    c+=1
s = False
if i==n:
    s = True
cnt = 0
for j in range(y+1, m+1):
    cnt += 1
    if s:
        if cnt%2:
            for i in range(n, 0, -1):
                print(i, j)
                grid[i][j] = c
                c+=1
        else:
            for i in range(1, n+1):
                print(i, j)
                grid[i][j] = c
                c+=1
    else:
        if cnt%2:
            for i in range(1, n+1):
                print(i, j)
                grid[i][j] = c
                c+=1
        else:
            for i in range(n, 0, -1):
                print(i, j)
                grid[i][j] = c
                c+=1
s = False
if i==n:
    s = True
cnt = 0
for j in range(1, y):
    cnt += 1
    if s:
        if cnt%2:
            for i in range(n, 0, -1):
                print(i, j)
                grid[i][j] = c
                c+=1
        else:
            for i in range(1, n+1):
                print(i, j)
                grid[i][j] = c
                c+=1
    else:
        if cnt%2:
            for i in range(1, n+1):
                print(i, j)
                grid[i][j] = c
                c+=1
        else:
            for i in range(n, 0, -1):
                print(i, j)
                grid[i][j] = c
                c+=1
#for i in grid: print(i)
