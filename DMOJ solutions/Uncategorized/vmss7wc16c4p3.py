import sys
input = sys.stdin.readline
D, I, R = map(int,input().split())
a,b = map(str,input().strip('\n').split())
n = len(a)
m = len(b)
dp = [[float('inf') for j in range(n+1)] for i in range(m+1)]
for i in range(n+1):
    dp[0][i] = i*D
for j in range(m+1):
    dp[j][0] = j*I
for i in range(1,m+1):
    for j in range(1,n+1):
        v = 0
        if a[j-1]!=b[i-1]:
            v = R
        dp[i][j] = min(dp[i-1][j]+I, dp[i][j-1]+D, dp[i-1][j-1] + v)
print(dp[m][n])