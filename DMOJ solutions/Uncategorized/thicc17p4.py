import sys
input = sys.stdin.readline
s = input().strip('\n')
n = len(s)
ans = float('inf')
for _ in range(int(input())):
    inp = input().split()
    t = int(inp[0])
    a = 0
    for k in inp[1:]:
        m = len(k)
        dp = [[float('inf') for j in range(m+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + int(s[i-1]!=k[j-1]))
        a += dp[n][m]
    ans = min(ans, float(a)/float(t))
print(round(ans, 6))