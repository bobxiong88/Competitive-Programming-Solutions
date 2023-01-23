import sys
input = sys.stdin.readline
def bs(x):
    l = 1
    r = 25997
    if x <= 2:
        return 1
    while l <= r:
        m = (l+r)//2
        if prime[m-1]<x<=prime[m]:
            return m
        if prime[m] > x:
            r = m-1
        else:
            l = m+1
    return "turtle"
def get(l, r):
    return psa[r]-psa[l-1]
mx = int(3e5)
sieve = [True]*mx
prime = [0]
x = 1
psa = [0]*mx
for i in range(2,mx):
    if sieve[i]:
        prime.append(i)
        psa[x] = psa[x-1]+i
        for j in range(2*i, mx, i):
            sieve[j] = False
        x += 1
Q = int(input())
for i in range(Q):
    x, k = map(int,input().split())
    g = bs(x)
    print(prime[g+k-1],get(g, g+k-1))