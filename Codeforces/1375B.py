import sys
input = sys.stdin.readline
t = int(input())
def check():
    for i in range(n):
        for j in range(m):
            if (i==0 and j==0) or (i==n-1 and j==m-1) or (i==0 and j==m-1) or(i==n-1 and j==0):
                if grid[i][j]>2:
                    return False
                else:
                    grid[i][j] = 2
            elif i==0 or j==0 or i==n-1 or j==m-1:
                if grid[i][j]>3:
                    return False
                else:
                    grid[i][j] = 3
            else:
                if grid[i][j]>4:
                    return False
                else:
                    grid[i][j] = 4
    return True
for _ in range(t):
    n, m = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int,input().split())))
    if check():
        print("YES")
        for row in grid:
            print(" ".join([str(x) for x in row]))
    else:
        print("NO")
