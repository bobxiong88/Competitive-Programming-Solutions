import sys
input = sys.stdin.readline
def rot(l):
    return [list(reversed(x)) for x in zip(*l)]
N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]
Q = int(input())
for _ in range(Q):
    r1,c1, r2, c2, x = map(int,input().split())
    x %= 360
    x//=90
    r1-=1
    c1-=1
    r2-=1
    c2-=1
    sub = []
    for i in range(r1, r2+1):
        sub.append(grid[i][c1:c2+1])
    n = r2-r1+1
    for k in range(x):
        sub = rot(sub)
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            grid[i][j] = sub[i-r1][j-c1]
for i in grid:
    print(*i)