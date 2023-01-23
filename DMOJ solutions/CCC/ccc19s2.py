import sys
input = sys.stdin.readline
p = []
sieve = [True for i in range(int(2e3)+1)]
for i in range(2,int(2e3)+1):
    if sieve[i]:
        p.append(i)
        for j in range(2*i, int(2e3)+1, i):
            sieve[j] = False
def prime(n):
    for i in p:
        if i>=n: break
        if n%i == 0: return False
    return True
for _ in range(int(input())):
    n = int(input())
    if prime(2) and prime(2*n-2):
        print(2, 2*n-2)
        continue
    for i in range(3, 2*n+1,2):
        if prime(i) and prime(2*n-i):
            print(i, 2*n-i)
            break