import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(list(input())[:m])
    c = 0
    for i in range(n):
        for j in range(m):
            if i==n-1 and grid[i][j] == 'D':
                c+=1
            if j==m-1 and grid[i][j] == 'R':
                c+=1
    print(c)
