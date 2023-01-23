import sys
input = sys.stdin.readline
n = int(input())
while n!=1:
    factors = []
    while n%2 == 0:
        n //= 2
        factors.append(2)
    for i in range(3,int(n**0.5)+1, 2):
        if n == 1: break
        while n%i == 0:
            n //= i
            factors.append(i)
    if n>1: factors.append(n)
    x = len(factors)
    a, b = 1,1
    for i in range(x//2): a*= factors[i]
    for i in range(x//2, x): b*=factors[i]
    print(a,b)
    sys.stdout.flush()
    n = int(input())