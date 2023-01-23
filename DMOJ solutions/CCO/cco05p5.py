import sys
input = sys.stdin.readline
N = int(input())
seg = [tuple(map(int,input().split())) for i in range(N)]
last = [seg[0][1]-seg[0][0]+seg[0][1],seg[0][1]-1]
#print(last)
for i in range(1, N):
    dp = [float('inf'), float('inf')]
    a, b = seg[i]
    for j in range(2):
        if a <= seg[i-1][j] <= b:
            dp[0] = min(dp[0], last[j]+b-a+b-seg[i-1][j])
            dp[1] = min(dp[1], last[j]+b-a+seg[i-1][j]-a)
        elif seg[i-1][j] < a:
            dp[0] = min(dp[0], last[j]+b-seg[i-1][j]+b-a)
            dp[1] = min(dp[1], last[j]+b-seg[i-1][j])
        else:
            dp[0] = min(dp[0], last[j]+seg[i-1][j]-a)
            dp[1] = min(dp[1], last[j]+seg[i-1][j]-a+b-a)
    last = dp[:]
ans = float('inf')
for i in range(2):
    ans = min(ans, N-seg[-1][i]+last[i])
ans += N-1
print(ans)