import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
dp = [0 for i in range(N)]
for i in range(1,N):
    res = float('inf')
    for j in range(1,3):
        if i-j<0: break
        res = min(res,dp[i-j]+abs(a[i]-a[i-j]))
    dp[i] = res
print(dp[N-1])