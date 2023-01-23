import sys
input = sys.stdin.readline
for _ in range(int(input())):
    trash = input()
    grid = [input().strip('\n') for i in range(8)]
    found = False
    for i in range(1,7):
        for j in range(1,7):
            if grid[i][j] == '#' and grid[i-1][j-1]=='#' and \
            grid[i-1][j+1]=='#' and grid[i+1][j+1]=='#' and grid[i+1][j-1]=='#':
                print(i+1,j+1)
                found = True
                break
        if found: break
    
