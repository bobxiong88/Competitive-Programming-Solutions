import sys
input = sys.stdin.readline
n = int(input())
grid = [input().strip('\n') for i in range(n)]
nxt = [[] for i in range(n)]
curr = [[] for i in range(n)]
ans = 0
for i in range(n-1,-1,-1):
    for j in range(n):
        if grid[i][j] == '.' or len(curr[j]) < 3:
            curr[j] = [0]
        curr[j] = min(curr[j])
        if grid[i][j] == '#':
            curr[j]+=1
        if i > 0:
            if j > 0:
                if grid[i-1][j-1] == '#': nxt[j-1].append(curr[j])
            if j < n-1:
                if grid[i-1][j+1] == '#': nxt[j+1].append(curr[j])
            if grid[i-1][j] == '#': nxt[j].append(curr[j])
        if grid[i][j] == '#': ans += curr[j]
    curr = nxt[:]
    nxt = [[] for i in range(n)]
print(ans)