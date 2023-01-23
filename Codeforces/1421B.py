import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    grid = [[]]
    for i in range(n):
        line = ' '+input().strip('\n')
        grid.append(line)
    a,b = grid[1][2], grid[2][1]
    x,y = grid[n][n-1], grid[n-1][n]
    if a == b and x == y and x!=a:
        print(0)
        continue
    if x == a == b == y:
        print(2)
        print(1,2)
        print(2,1)
        continue
    ans = []
    if a != b:
        if x == y:
            if b != x:
                a = b
                ans.append((1,2))
            else:
                b = a
                ans.append((2,1))
        else:
            a = b
            ans.append((1,2))
    if x == a:
        ans.append((n,n-1))
    elif y == b:
        ans.append((n-1,n))
    print(len(ans))
    for i in ans: print(*i)
