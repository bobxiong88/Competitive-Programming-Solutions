import sys
input = sys.stdin.readline
N, X = map(int,input().split())
sieve = [True]*(N+1)
sieve[0] = False
sieve[1] = False
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for x in range(2*i, N+1, i):
            sieve[x] = False
primes = []
for i in range(N+1):
    if sieve[i]:
        primes.append(i)
t = 0
for prime in primes:
    r = N-prime
    t+=r//X+1
    t+=(r-1)//X+1
print(t)