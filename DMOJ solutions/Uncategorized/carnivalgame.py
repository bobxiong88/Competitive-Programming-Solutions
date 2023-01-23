import sys
input = sys.stdin.readline
N = int(input())
grid = []
for i in range(N-1):
    grid.append(input().strip('\n'))
dp = [[float('inf')]*N for j in range(N)]
a = list(map(int,input().split()))
dp[0][0] = 0
flip = [[0 for i in range(N)] for i in range(N)]
par = [[0 for i in range(N)] for j in range(N)]
for i in range(N-1):
    for j in range(i+1):
        if dp[i+1][j] > dp[i][j]+(grid[i][j]=='R'):
            dp[i+1][j] = dp[i][j]+(grid[i][j]=='R')
            par[i+1][j] = j
            flip[i+1][j] = grid[i][j]=='R'
        if dp[i+1][j+1] > dp[i][j]+(grid[i][j]=='L'):
            dp[i+1][j+1] = dp[i][j]+(grid[i][j]=='L')
            par[i+1][j+1] = j
            flip[i+1][j+1] = grid[i][j]=='L'

res = (-float('inf'), 0)
for j in range(N):
    res = max(res, (a[j]-dp[N-1][j], j))
j = res[1]
print(res[0])
print(dp[N-1][j])
cnt = 0
for i in range(N-1, 0, -1):
    if flip[i][j]:
        print(i,par[i][j]+1)
    j = par[i][j]
'''
10
R
RL
LRL
RLRL
RRRRR
RLRLRL
RLRLRLR
LLLLLLRR
LRLRLLRLR
3 4 -1 3 9 4 5 -10 2 5
'''