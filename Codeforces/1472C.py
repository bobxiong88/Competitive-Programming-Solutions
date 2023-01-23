import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = max(a)
    dp = a[:]
    graph = [[] for i in range(n)]
    for i in range(n):
        if a[i]+i<n:
            dp[a[i]+i] = max(a[a[i]+i]+dp[i],dp[a[i]+i])
    print(max(dp))
