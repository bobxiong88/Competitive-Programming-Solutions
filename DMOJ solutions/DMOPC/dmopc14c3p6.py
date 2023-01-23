import sys
input = sys.stdin.readline
n,t = map(int,input().split())
dp = [0 for i in range(t+1)] 
for i in range(n):
    pp, vp, pa, va, pg, vg = map(int,input().split())
    for j in range(t, -1, -1):
        if pp+j <= t:
            dp[j+pp] = max(vp + dp[j], dp[j+pp])
        if pa+j <= t:
            dp[j+pa] = max(va + dp[j], dp[j+pa])
        if pg+j <= t:
            dp[j+pg] = max(vg + dp[j], dp[j+pg])
print(dp[t])