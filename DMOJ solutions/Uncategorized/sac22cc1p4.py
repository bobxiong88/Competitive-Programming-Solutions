import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
dp = [[0]*101 for i in range(3)]
# dp[i][j] = number of ways to reach value j using i numbers
ans = 0
for i in range(N):
    for x in range(2,0,-1):
        for j in range(101):
            if j-a[i]>=0:
                dp[x][j] += dp[x-1][j-a[i]]
    dp[0][a[i]] += 1
    ans += dp[2][a[i]] # number of ways to reach A[i] with 3 numbers
print(ans)