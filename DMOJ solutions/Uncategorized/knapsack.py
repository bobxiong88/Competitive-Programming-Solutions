import sys
input = sys.stdin.readline
from math import log
from math import ceil
N, M = map(int,input().split())
dp = [0]*5005
for _ in range(N):
    n, v, p = map(int,input().split())
    b = ceil(log(n,2))+1
    for x in range(b):
        k = min(n, 2**x)
        if k <= 0: break
        n -= 2**x
        w,c = k*v, k*p
        for i in range(5004-w,-1,-1):
            dp[i+w] = max(dp[i]+c, dp[i+w])
ans = -float('inf')
for i in range(M):
    c,f = map(int,input().split())
    ans = max(ans, dp[c]-f)
print(ans)