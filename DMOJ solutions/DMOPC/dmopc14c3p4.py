import sys
input = sys.stdin.readline
sieve = [0]*(100001)
for i in range(1,100001):
    for j in range(i,100001,i):
        sieve[j]+=1
count = [[0 for i in range(129)] for i in range(100001)]
total = [0]*129
for i in range(1,100001):
    for j in range(1,129):
        if sieve[i] == j:
            total[j]+=1
        count[i][j] = total[j]
T = int(input())
for i in range(T):
    K, A, B = map(int,input().split())
    if K>128:
        print(0)
        continue
    print(count[B][K]-count[A-1][K])