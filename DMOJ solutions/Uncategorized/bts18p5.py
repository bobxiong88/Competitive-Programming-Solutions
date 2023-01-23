import sys
input = sys.stdin.readline
m = 119*(2**23)+1
n = int(input())
a = list(map(int,input().split()))
dp = [[0 for i in range(n)] for j in range(n)]
s = 0
for i in range(n):
    s += a[i]
    s %= m
    dp[0][i] = s
c = a[0]
ans = [dp[0][-1]]
for k in range(1,n):
    c *= a[k]
    c %= m
    dp[k][k] = c
    for i in range(k+1,n):
        dp[k][i] = dp[k-1][i-1]*a[i]+dp[k][i-1]
        dp[k][i] %= m
    ans.append(dp[k][-1])
print(*ans)