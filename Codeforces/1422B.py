import sys
from math import floor
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int,input().split())
    grid = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(ceil(n/2)):
        for j in range(ceil(m/2)):
            pog = [grid[i][j],grid[i][m-j-1],grid[n-i-1][j],grid[n-i-1][m-j-1]]
            if i == n-i-1:
                pog = pog[:2]
            elif j==m-j-1:
                pog = pog[::2]
            curr = float('inf')
            for a in pog:
                x = 0
                for b in pog:
                    x+=abs(a-b)
                curr = min(x,curr)
            ans += curr
    print(ans)
