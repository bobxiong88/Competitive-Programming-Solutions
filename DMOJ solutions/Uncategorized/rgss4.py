import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for i in range(N)]
dp = A[:]
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + A[i]:
            dp[i] = dp[j] + A[i]
print(max(dp))