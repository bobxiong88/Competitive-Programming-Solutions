import sys
input = sys.stdin.readline
sieve = [True]*(1000001)
sieve[0],sieve[1] = False,False
s = 0
prefix = []
for i in range(1000001):
    if sieve[i]:
        s+=1
        if i<=1001:
            for j in range(2*i,1000001,i):
                sieve[j] = False
    prefix.append(s)
N = int(input())
for _ in range(N):
    A,B = map(int,input().split())
    print(prefix[B-1]-prefix[A-1])