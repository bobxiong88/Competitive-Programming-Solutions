import sys
input = sys.stdin.readline
for  _ in range(int(input())):
    n, k = map(int,input().split())
    s = input().strip('\n')
    dp = [float('inf')]*n
    x = s.index('*')
    dp[x] = 1
    last = dp[x]
    for i in range(x+1, n):
        if s[i] == '*':
            for j in range(i-k, i):
                if s[j] == '*':
                    dp[i] = min(dp[i], dp[j]+1)
            last = dp[i]
    print(last)
