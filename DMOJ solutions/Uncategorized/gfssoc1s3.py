import sys
input = sys.stdin.readline
def dfs(node):
    x,y = node
    for i, j in [(1,0),(0,1),(-1,0),(0,-1)]:
        i += x
        j += y
        if not(0 <= i < N and 0 <= j < M): continue
        if not(dist[x][y] + 1 < dist[i][j] and grid[i][j] != 'X'): continue
        dist[i][j] = dist[x][y] + 1
        dfs((i,j))
def solve(curr, ans):
    if len(curr) == len(a):
        c.append(ans)
        return
    for i in range(T+1):
        if i not in curr:
            solve(curr+[i], ans + da[curr[-1]][a[i][0]][a[i][1]])
N, M, T = map(int,input().split())
grid = [input().strip('\n') for i in range(N)]
a = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'H': a.append((i,j))
        if grid[i][j] == 'G': a.insert(0,(i,j))
da = []
for x,y in a:
    dist = [[float('inf')]*M for i in range(N)]
    dist[x][y] = 0
    dfs((x,y))
    da.append(dist)
c = []
solve([0], 0)
print(min(c))