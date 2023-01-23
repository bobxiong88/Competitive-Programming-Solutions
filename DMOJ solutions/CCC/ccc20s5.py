import sys
input = sys.stdin.readline
N = int(input())
b = list(map(int,input().split()))
if b[0] == b[-1]:
    print(1)
    sys.exit(0)
dp = [0 for i in range(N)]
last = [-1 for i in range(500005)]
s = 0
for i in range(N-1, -1, -1):
    if i == N-1:
        pass
    elif i and b[0] == b[i]:
        dp[i] = 1
    elif i and last[b[i]]!=-1:
        dp[i] = dp[last[b[i]]]
    else:
        dp[i] = (1+s)/(N-i)
    last[b[i]] = i
    s += dp[i]
print(dp[i])