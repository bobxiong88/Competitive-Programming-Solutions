import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    a = 0
    grid = []
    for i in range(n):
        line = list(map(int,input().split()))
        grid.append(line)
    c=0
    while True:
        c+=1
        found = False
        for i in range(n):
            for j in range(m):
                if 1 not in grid[i] and 1 not in [grid[x][j] for x in range(n)]:
                    grid[i][j] = 1
                    found = True
                    break
            if found:
                break
        if not found:
            break
    if c%2==0:
        print("Ashish")
    else:
        print("Vivek")
