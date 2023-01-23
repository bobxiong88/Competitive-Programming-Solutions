import sys
input = sys.stdin.readline
X = int(input())
N = int(input())
dp = [float('inf')]*(X+1)
values = []
dp[0] = 0
for _ in range(N):
    value = int(input())
    for i in range(value, X+1):
        dp[i] = min(dp[i], dp[i-value]+1)
print(dp[X])