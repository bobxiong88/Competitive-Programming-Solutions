import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
def dfs(i,j):
    if dp[i][j]!=0:
        return dp[i][j]
    m = 0
    for x,y in (i+1,j),(i,j+1),(i-1,j),(i,j-1):
        if 0<=x<N and 0<=y<N and grid[x][y] > grid[i][j]:
            p = 1 + dfs(x,y)
            m = max(m,p)
    dp[i][j] = m
    return m

N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int,input().split())))
dp = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        dfs(i,j)
print(max([max(row) for row  in dp]))