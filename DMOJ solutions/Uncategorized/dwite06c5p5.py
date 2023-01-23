import sys
input = sys.stdin.readline
sieve = [True]*(1000000)
prime = []
for i in range(2, 1000000):
    if sieve[i]:
        for j in range(2*i, 1000000, i):
            sieve[j] = False
        i = str(i)
        if i[:len(i)//2]==i[len(i)//2+len(i)%2:][::-1]:
            prime.append(int(i))
for _ in range(5):
    a,b = map(int,input().split())
    c = 0
    for i in prime:
        if i>b:
            break
        if i>=a:
            c+=1
    print(c)