import sys
input = sys.stdin.readline
n = int(input())
dp = [int(input()) for i in range(n)]
for i in range(n):
    if not i: continue
    for j in range(i):
        dp[i] = max(dp[i-j-1]+dp[j], dp[i])
print(dp[-1])