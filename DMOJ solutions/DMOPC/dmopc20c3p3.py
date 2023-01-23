import sys
input = sys.stdin.readline
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return -1
    else:
        return x % m
def div(a, b, m):
    a = a%m
    b = b%m
    inv = modinv(b,m)
    if inv == -1:
        return 0/0
    else:
        return (inv*a)%m
m = int(1e9)+7
for _ in range(int(input())):
    N, M, K, B = map(int,input().split())
    if K == 1:
        if N%3 == 0:
            res = div((B**2)*(M)*(1-pow(B**3, N//3, m)),1-B**3, m)
        elif M%3 == 0:
            res = div((M//3)*(1-pow(B, N, m)),1-B, m)
        else:
            res = -1
    elif K == 2:
        if M%2 or (N*M)%4:
            res = -1
        elif N%2:
            res = div((M//4)*(1-pow(B, N, m)),1-B, m)
        else:
            x = N*M//4
            res = div(B*(x//(N//2))*(1-pow(B**2, N//2, m)),1-B**2, m)
    else:
        if M%(K+2):
            res = -1
        else:
            x = M//(K+2)
            res = div(x*(1-pow(B, N, m)),1-B, m)
    print(res)