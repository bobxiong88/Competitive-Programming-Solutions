import sys
input = sys.stdin.readline
m = 10007
last = [-1 for i in range(256)]
s = input().strip('\n')
n = len(s)
dp = [0 for i in range(n+1)]
dp[0] = 1
for i in range(1,n+1):
    dp[i] = 2*dp[i-1]%m
    if last[ord(s[i-1])] != -1:
        dp[i] -= dp[last[ord(s[i-1])]]
    last[ord(s[i-1])] = i-1
print((dp[n]-1)%m)