import sys
input = sys.stdin.readline
n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mx = 2**9
dp = [[0 for i in range(mx)] for i in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(mx):
        if dp[i][j]:
            for x in b:
                dp[i+1][j|(a[i]&x)] = 1
for i in range(mx):
    if dp[n][i]:
        print(i)
        sys.exit(0)
