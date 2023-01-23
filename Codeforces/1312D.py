import sys
input = sys.stdin.readline
n, m = map(int,input().split())
mod = 998244353
a = b = 1
for i in range(min(m, m-(n-1))):
    a = (a*(m-i))%mod
    b = (b*(i+1))%mod
ans = (a*pow(b, mod-2, mod))%mod
for i in range(n-3):
    ans = (ans*2)%mod
print((ans*(n-2))%mod)
