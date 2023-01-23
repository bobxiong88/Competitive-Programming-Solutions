import sys
input = sys.stdin.readline
def f(n, mod):
    if n>=mod:
        return 0
    if n>=34:
        return 0 
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i)%mod
    return ans
N = int(input())
for i in range(N):
    print(f(int(input()), 2**32))