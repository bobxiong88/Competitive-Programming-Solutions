for _ in range(5):
    N = int(input())
    dp = [False]*1441
    dp[0] = True
    for i in range(N):
        S = int(input())
        for i in range(1440-S, -1, -1):
            if dp[i]:
                dp[i+S] = True
    ans = 0
    for i in range(1441):
        if dp[i]:
            ans = i
    print(1440-ans)