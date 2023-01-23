import sys
input = sys.stdin.readline
N, K = map(int,input().split())
sieve = [True]*(N+1)
sieve[0],sieve[1] = False,False
primes = []
dp = [float('inf')]*(N+1)
for i in range(2,N+1):
    if sieve[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            sieve[j] = False
dp[0] = 0
c = 0
for i in range(N+1):
    if dp[i]==K:c+=1
    for p in primes:
        if i+p<=N:
            dp[i+p] = min(dp[i]+1,dp[i+p])
print(c)