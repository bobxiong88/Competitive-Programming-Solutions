N = int(input())
sieve = [True for i in range(10000)]
c = 0
for i in range(2,10000):
    if c==N: break
    if sieve[i]:
        print(i)
        c+=1
        for j in range(2*i, 10000, i):
            sieve[j] = False