import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [[0,0,0] for i in range(n)]
dp[0][0] = b[0]
dp[0][1] = a[0]
dp[0][2] = a[0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])+b[i]
    dp[i][1] = dp[i-1][0]+a[i]
    dp[i][2] = dp[i-1][1]+a[i]
print(max(dp[-1]))