import sys
input = sys.stdin.readline
mx = int(1e5)+5
sieve = [True]*(mx)
prime = []
for i in range(2,mx):
    if sieve[i]:
        prime.append(i)
        for j in range(i*2, mx, i):
            sieve[j] = False
for _ in range(int(input())):
    d = int(input())
    for i in prime:
        if i-1 >= d:
            x = i
            break
    for i in prime:
        if i-x >= d and i*x-i >= d:
            print(i*x)
            break
    
