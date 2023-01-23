import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
dp = [0 for i in range(n)]
m = -float('inf')
for i in range(n):
    m = max(a[i], m)
    dp[i] = dp[i-1]+m-a[i]
gay = [0 for i in range(n)]
a = a[::-1]
m = -float('inf')
for i in range(n):
    m = max(a[i],m)
    gay[i] = gay[i-1]+m-a[i]
gay = gay[::-1]
ans = float('inf')
for i in range(n-1):
    ans = min(ans, dp[i]+gay[i+1])
print(ans)