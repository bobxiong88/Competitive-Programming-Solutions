import sys
input = sys.stdin.readline
n = int(input())
s = 0
m = 998244353
a = 1
for i in range(n,1,-1):
    a*=i
    a%=m
    s+=a
    s%=m
b = 1
for i in range(1,n+1):
    b*=i
    b%=m
print((b*n-s)%m)
