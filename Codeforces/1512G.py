import sys
input = sys.stdin.readline
mx = int(1e7)+1
ans = [-1]*mx
sieve = [0]*mx
i = 1
while i < mx:
    j = i
    while j < mx:
        sieve[j] += i
        j += i
    if sieve[i] < mx and ans[sieve[i]] == -1:
        ans[sieve[i]] = i
    i+=1
for _ in range(int(input())):
    print(ans[int(input())])
