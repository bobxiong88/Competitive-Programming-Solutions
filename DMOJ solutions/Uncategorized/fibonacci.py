import sys

sys.setrecursionlimit(2000000000)

a,b,c,d = 0,0,0,0

def fib(n):
    if n == 0:
        yield (0, 1)
    else:
        bruh = list(fib(n//2))
        a, b = bruh[0]
        c = (a * (b * 2 - a))%1000000007
        d = (a * a + b * b)%1000000007
        if n % 2 == 0:
            yield (c, d)
        else:
            yield (d, c + d)
input = sys.stdin.readline
n = int(input())

print(list(fib(n))[0][0])
