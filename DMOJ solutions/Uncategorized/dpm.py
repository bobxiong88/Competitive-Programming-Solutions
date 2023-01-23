import sys
input = sys.stdin.readline
N, K = map(int,input().split())
a = list(map(int,input().split()))
dp = [[0]*(K+1) for i in range(N)]
m = int(1e9)+7
for i in range(K-a[0], K+1):
    dp[0][i] = 1
for i in range(N-1):
    for j in range(K+1):
        dp[i+1][max(0, j-a[i+1])] += dp[i][j]
        if j != K: dp[i+1][j+1] -= dp[i][j]
    for j in range(1,K+1):
        dp[i+1][j] += dp[i+1][j-1]
        dp[i+1][j] %= m
print(dp[-1][0]%m)