import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    dp = [[0,0] for i in range(n)] # split, no split
    for i in range(1,n):
        if a[i] < a[i-1]:
            dp[i][0] = dp[i-1][1]+1
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = max(dp[i-1])
            dp[i][1] = max(dp[i-1])
    print(max(dp[-1]))
