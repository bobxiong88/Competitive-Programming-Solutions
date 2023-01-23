import sys
input = sys.stdin.readline
def check():
    if grid[0][0] > grid[0][1]:
        return False
    if grid[0][0] > grid[1][0]:
        return False
    return True
n = int(input())
grid = [list(map(int,input().split())) for i in range(n)]
for _ in range(4):
    if check():
        for row in grid:
            print(" ".join([str(i) for i in row]))
        break
    new = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n-i-1] = grid[i][j]
    grid = new[:]