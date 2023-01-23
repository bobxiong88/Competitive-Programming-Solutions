import sys
input = sys.stdin.readline
N = int(input())
dp = [[0,0,0] for i in range(N)]
a = [tuple(map(int,input().split())) for i in range(N)]
if N == 1:
    print(max(a[0]))
    sys.exit(0)
for i in range(N):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2])+a[i][0]
    dp[i][1] = max(dp[i-1][0],dp[i-1][2])+a[i][1]
    dp[i][2] = max(dp[i-1][1],dp[i-1][0])+a[i][2]
print(max(dp[-1]))