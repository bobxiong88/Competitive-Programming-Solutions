# dp[j][i] = max value at i given that you're currently on the jth interval
# dp[1][0] = a[0]%p
# dp[j][i] = max(dp[j-1][j-1...i-1]+sum(a[j-1...i-1:i])%p)
# observation: p, k are small!



import sys
input = sys.stdin.readline
N, k, p = map(int,input().split())
a = list(map(int,input().split()))
dp = [[0]*N for i in range(k+1)]
dp[1][0] = a[0]%p
for i in range(1,N):
    for j in range(1, min(i+1, k)+1):
        if j == 1:
            dp[j][i] = sum(a[:i+1])%p
        else:
            dp[j][i] = max([dp[j-1][x]+sum(a[x+1:i+1])%p for x in range(j-1, i+1)])
print(dp[k][-1])
