N,K = map(int,input().split())
f = list(map(int,input().split()))
fishes = [0]*(N+1)
for i in f:
    fishes[i]+=1
    
dp = [[0]*(K+1) for i in range(N+1)]
dp[0][0] = 1
for n in range(1,N+1):
    dp[n][0] = 1
    for k in range(1,K+1):
        dp[n][k] = dp[n-1][k]+fishes[n]*dp[n-1][k-1]

print(dp[N][K]%998244353)