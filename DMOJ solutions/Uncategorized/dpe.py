import sys
input = sys.stdin.readline
N, W = map(int,input().split())
dp = [float('inf')]*100005
dp[0] = 0
ans = 0
for x in range(N):
    w,v = map(int,input().split())
    for i in range(100004, -1, -1):
        if dp[i]+w <= W:
            dp[i+v] = min(dp[i+v], dp[i]+w)
            ans = max(ans, i+v)
print(ans)