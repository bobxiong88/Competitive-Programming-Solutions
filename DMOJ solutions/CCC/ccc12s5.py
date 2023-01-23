import sys
input = sys.stdin.readline
r,c = map(int,input().split())
k = int(input())
cage = [[False for i in range(c)] for j in range(r)]
for i in range(k):
    a,b = map(int,input().split())
    a-=1
    b-=1
    cage[a][b] = True
dp = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        if i or j:
            if not cage[i][j]:
                s = 0
                if i-1>=0: s += dp[i-1][j]
                if j-1>=0: s += dp[i][j-1]
                dp[i][j] = s
        else:
            dp[i][j] = 1
print(dp[-1][-1])