import sys
input = sys.stdin.readline
N, M = map(int,input().split())
grid = []
for i in range(N):
    grid.append(input().strip('\n'))
prow = []
for i in range(N):
    curr = [0]
    for j in range(M):
        curr.append((grid[i][j]=='*')+curr[-1])
    prow.append(curr[:])
pcol = []
for j in range(M):
    curr = [0]
    for i in range(N):
        curr.append((grid[i][j] == '*')+curr[-1])
    pcol.append(curr)
ans = 0
def get(psa, i, j):
    return psa[j]-psa[i-1]
for i in range(1, N+1):
    for j in range(1, M+1):
        if grid[i-1][j-1] == '*': continue
        if get(prow[i-1], 1, j-1) >= 2 or get(prow[i-1], j+1, M) >= 2 \
        or get(pcol[j-1], 1, i-1) >= 2 or get(pcol[j-1], i+1, N) >= 2:
            ans += 1
print(ans)