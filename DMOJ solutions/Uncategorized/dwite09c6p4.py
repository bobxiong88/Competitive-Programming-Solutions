for _ in range(5):
    V = int(input())
    N = int(input())
    coins = []
    dp = [float('inf')]*(V+1)
    dp[0]=0
    for i in range(N):
        coins.append(int(input()))
    for i in range(1,V+1):
        for coin in coins:
            if coin<=i:
                amount = dp[i-coin]
                if amount!=float('inf')and amount+1<dp[i]:
                    dp[i]=amount+1
    print(dp[V])