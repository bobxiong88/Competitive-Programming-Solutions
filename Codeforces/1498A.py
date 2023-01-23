import sys
input = sys.stdin.readline
def gcd(a, b):
    if a == 0: return b
    return gcd(b%a,a)
for _ in range(int(input())):
    n = int(input())
    while True:
        s = sum([int(i) for i in str(n)])
        if gcd(n, s) > 1:
            print(n)
            break
        n+=1
