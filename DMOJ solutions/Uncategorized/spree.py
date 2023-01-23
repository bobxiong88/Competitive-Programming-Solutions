N, W = map(int,input().split())

dp = [0]*(W+1)

for _ in range(N):
    value, weight = map(int,input().split())
    
    for x in range(W-weight,-1,-1):
        
        dp[x+weight] = max(dp[x+weight],dp[x]+value)
print(max(dp))