import sys
input = sys.stdin.readline
N, W = map(int,input().split())
dp = [0]*(W+1)
for i in range(N):
    w, v = map(int,input().split())
    for x in range(W, w-1, -1):
        dp[x] = max(dp[x], dp[x-w]+v)
print(max(dp))