import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m,x,y = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    c = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                if j<m-1:
                    if grid[i][j+1] == '.':    
                        if x*2>=y:
                            grid[i][j] = '*'
                            grid[i][j+1] = '*'
                            c+=y
                            continue
                grid[i][j] = '*'
                c+=x
    print(c)
