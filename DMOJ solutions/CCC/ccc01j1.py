import sys
input = sys.stdin.readline
n = int(input())
grid = [[' ']*n for i in range(n)]
for i in range(1,n,2):
    for j in range((i+1)//2,n-(i+1)//2):
        grid[j][i] = '*'
        grid[j][i+1] = '*'
for i in range(n):
    grid[i][0] = '*'
for i in range(n):
    print(''.join(grid[i]+grid[i][::-1]))