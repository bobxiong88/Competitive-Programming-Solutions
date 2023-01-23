import sys
input = sys.stdin.readline
M, U, R = map(int,input().split())
dp = [[0 for i in range(U+1)] for j in range(M+1)]
for _ in range(R):
    V, T, F = map(int,input().split())
    for i in range(M-T, -1, -1):
        for j in range(U-F, -1, -1):
            dp[i+T][j+F] = max(V+dp[i][j], dp[i+T][j+F])
print(dp[M][U])