import sys
input = sys.stdin.readline
def gcd(a,b):
    if a == 0: return b
    return gcd(b%a, a)
def check(prime):
    for i in a:
        if i%prime: return False
    return True
p = [True]*(1000)
primes = []
for i in range(2,1000):
    if p[i]:
        primes.append(i)
        for j in range(i+i, 1000, i):
            p[j] = False
N = int(input())
a = list(map(int,input().split()))
a = [abs(i) for i in a]
ans = 1
for prime in primes:
    while check(prime):
        ans*=prime
        for i in range(N):
            a[i] //=prime
print(ans)