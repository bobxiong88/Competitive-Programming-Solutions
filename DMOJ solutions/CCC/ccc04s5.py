import sys
input = sys.stdin.readline
def dfs(x,y):
    for i,j in [(1,0),(0,1),(-1,0)]:
        i+=x
        j+=y
        if 0<=i<m and 0<=j<n:
            if not vis[i][j] and grid[i][j]!='*':
                vis[i][j] = True
                dfs(i,j)
while True:
    m,n = map(int,input().split())
    if not m: break
    dp = [[0 for i in range(n)] for i in range(m)]
    grid = []
    for i in range(m):
        line = input().strip('\n')
        new = []
        for j in range(n):
            if line[j] == '*': new.append('*')
            elif line[j] == '.': new.append(0)
            else: new.append(int(line[j]))
        grid.append(new)
    for i in range(m-1, -1, -1):
        if grid[i][0] == '*': break
        dp[i][0] = dp[(i+1)%m][0]+grid[i][0]
    vis = [[False]*n for i in range(m)]
    vis[m-1][0] = True
    dfs(m-1,0)
    for j in range(1,n):
        for i in range(m):
            if not vis[i][j]: continue
            if not vis[i][j-1]: continue
            if grid[i][j-1] == '*': continue
            if grid[i][j] == '*': continue
            new = [0]*m
            new[i] = dp[i][j-1]+grid[i][j]
            for k in range(i+1,m):
                if grid[k][j] == '*': break
                new[k] = new[k-1]+grid[k][j]
            for k in range(i-1, -1, -1):
                if grid[k][j] == '*': break
                new[k] = new[k+1]+grid[k][j]
            for k in range(m):
                dp[k][j] = max(dp[k][j], new[k])
    print(dp[m-1][n-1])