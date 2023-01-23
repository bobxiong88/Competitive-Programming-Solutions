import sys
input = sys.stdin.readline
def long(N, A):
    dp = [1]*N
    s = 1
    for i in range(N):
        for j in range(i):
            if (A[j] < A[i]):
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
for _ in range(int(input())):
    n = int(input())
    a = [0]+list(map(int,input().split()))
    dp = [1]*(n+1)
    for i in range(1, n+1):
        for j in range(i*2, n+1, i):
            if a[i] < a[j]:
                dp[j] = max(dp[j], dp[i]+1)
    print(max(dp))
