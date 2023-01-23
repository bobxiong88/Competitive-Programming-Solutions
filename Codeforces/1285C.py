import sys
input = sys.stdin.readline
x = int(input())
factors = []
def gcd(a,b):
    if a == 0: return b
    return gcd(b%a, a)
def lcm(a,b):
    return a*b//gcd(a,b)
for i in range(1,int(x**0.5)+1):
    if x%i == 0: factors.append((i,x//i))
ans = (1,x)
for a,b in factors:
    if lcm(a,b) == x:
        ans = (a,b)
print(*ans)
