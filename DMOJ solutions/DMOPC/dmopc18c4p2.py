import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
K = sum(A)
dp = [-1 for i in range(K+1)]
dp[0] = float('inf')
for i in range(N):
    for j in range(A[i], K+1):
        if dp[j] == -1 and dp[j-A[i]] != i and dp[j-A[i]] != -1:
            dp[j] = i
ans = float('inf')
for i in range(K+1):
    if dp[i]!=-1:
        ans = min(ans, abs(K-2*i))
print(ans)