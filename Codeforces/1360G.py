import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, a, b = map(int,input().split())
    if a*n!=b*m:
        print('NO')
        continue
    print('YES')
    for s in range(m):
        found = True
        grid = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(a):
                grid[i][(j+s*i)%m] = 1
        for j in range(m):
            c = 0
            for i in range(n):
                c+=grid[i][j]
            if c!=b: found = False
        #for row in grid: print(''.join([str(i) for i in row]))
        if found:
            for row in grid: print(''.join([str(i) for i in row]))
            break
