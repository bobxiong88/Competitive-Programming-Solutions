import sys
input = sys.stdin.readline
'''
mx = int(3e6)
prime = []
sieve = [True]*mx
for i in range(2,mx):
    if not sieve[i]: continue
    prime.append(i)
    for j in range(2*i, mx, i):
        sieve[j] = False
'''
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pog = set()
    if n == 1:
        print(0)
        continue
    m = float('inf')
    x = 0
    for i in range(n):
        if a[i] < m:
            m = a[i]
            x = i
    print(n-1)
    k = 0
    for i in range(x+1, n):
        k+=1
        print(x+1,i+1,a[x],a[x]+k)
    k=0
    for i in range(x-1, -1, -1):
        k+=1
        print(x+1,i+1,a[x],a[x]+k)
        
