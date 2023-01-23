import sys
input = sys.stdin.readline
def gcd(a,b):
    if a == 0: return b
    return gcd(b%a, a)
def lcm(a,b):
    return (a*b)//gcd(a,b)
for _ in range(int(input())):
    n = int(input())
    a = 1
    b = 1
    ans = 0
    m = int(1e9)+7
    for i in range(2, 500):
        b = lcm(b, i)
        
        ans += i*(n//a-n//b)
        ans %= m
        if b>n: break
        a = lcm(a, i)
    print(ans)
2,5,7,10,12,16,18
