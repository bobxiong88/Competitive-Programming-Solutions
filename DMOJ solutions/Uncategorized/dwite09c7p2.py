sieve = [False]*(100001)
sieve[0],sieve[1] = True, True
for i in range(2, 317):
    if not sieve[i]:
        for j in range(2*i, 100001, i):
            sieve[j] = True
prefix = [0]*(100001)
s = 0
for i in range(2,100001):
    if not sieve[i]:
        s+=i
    prefix[i] = s
for i in range(5):
    print(prefix[int(input())])