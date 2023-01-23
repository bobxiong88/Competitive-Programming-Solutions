import sys
input = sys.stdin.readline
mx = int(2e6)+1
def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)
def inv(a, m):
    g = gcd(a, m)
    if g != 1: return -1
    return pow(a, m-2, m)
def div(a, b, m):
    a %= m
    pog = inv(b, m)
    if pog == -1: print("bosnian burping scissors")
    return (pog*a)%m
def f(n):
    return tb[n]
def c(n, r):
    return div(f(n),f(r)*f(n-r),m)
m = 998244353
tb = [1]*mx
for i in range(2,mx):
    tb[i] = tb[i-1]*i
    tb[i]%= m
for _ in range(int(input())):
    N, K, Q = map(int,input().split())
    r = N-K*Q
    r -= Q-1
    if r<0: print(0)
    else: print(c(r+Q,Q)%m)