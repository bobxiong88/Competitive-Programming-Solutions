import sys
input = sys.stdin.readline
def gcd(a,b):
    if a == 0: return b
    return gcd(b%a, a)
N = int(input())
num = list(map(int,input().split()))
g = num[0]
for n in num:
    g = gcd(g, n)
if g == 1:
    print("DNE")
else:
    prime = 2
    for i in range(2, int(g**0.5)+1):
        while g % i == 0:
            prime = i
            g /= i
    prime = max(g, prime)
    print(int(prime))