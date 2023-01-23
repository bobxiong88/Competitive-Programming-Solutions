N = int(input())

a = list(map(int,input().split()))

dp = [[0]*(N+1) for i in range(N+1)]

for L in range(N, -1, -1):
    for R in range(L, N):
        if L==R:
            dp[L][R] = a[L]
        else:
            dp[L][R] = max(a[L]-dp[L+1][R],a[R]-dp[L][R-1])
print(dp[0][N-1])