N = int(input())
dp = [0]*(N+1)
dp[0]=1
coins = list(map(float,input().split()))
coin=0
for p in coins:
    for i in range(coin+1,-1,-1):
        if i==0:
            dp[i]=dp[i]*(1-p)
        else:
            dp[i]=dp[i-1]*p+dp[i]*(1-p)
    coin+=1
p = 0
for i in range(1,N+1):
    tails = N-i
    if i>tails:
        p+=dp[i]
print(p)