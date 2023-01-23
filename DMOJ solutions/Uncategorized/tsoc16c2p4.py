import sys
input = sys.stdin.readline
def prime(x):
    if x < 2: return False
    if x == 2: return True
    for i in range(2, int(x**0.5)+1):
        if x%i == 0: return False
    return True
n = int(input())
m = int(input())
items = []
s = 0
for i in range(m):
    m = int(input())
    items.append(m)
    s += m
s*=2
if s>n:
    print("not primetime")
    sys.exit(0)
primes = []
for i in range(1, n+1):
    if prime(i): primes.append(i)
a = [False]*(n+1)
a[s] = True
for item in items:
    for i in range(len(primes)-1, -1, -1):
        for j in primes:
            v = primes[i]-j*item
            if v >= s:
                if a[v] == True:
                    a[primes[i]] = True
                    break
            else:
                break
grid = [False]*(n+1)
for i in range(s,n+1):
    if a[i] and i in primes:
        print("its primetime")
        sys.exit(0)
print("not primetime")