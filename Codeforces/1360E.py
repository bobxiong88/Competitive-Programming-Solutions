import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    grid = [list(map(int,list(input().strip('\n')))) for i in range(n)]
    ans = True
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                if i+1>=n: a = True
                else: a = grid[i+1][j]
                if j+1>=n: b = True
                else: b = grid[i][j+1]
                if not(a or b): ans = False
    if ans: print('YES')
    else: print('NO')
                
