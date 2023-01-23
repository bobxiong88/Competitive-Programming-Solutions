import sys
input = sys.stdin.readline
C, D, K = map(int,input().split())
coins = [tuple(map(float,input().split())) for i in range(D)]
c = [i[:] for i in coins]
coins.sort(reverse = True)
mx = int(1e5)+5
make = [0]*mx
for i in range(mx):
    curr = i
    for v, w in coins:
        make[i] += (curr//v)*w
        curr -= curr//v*v
        if not curr: break
dp = [float('inf')]*mx
s = 0
pog = []
for _ in range(K):
    x = int(input())
    s += c[x-1][1]
    pog.append(c[x-1])
dp[0] = s
for v, w in pog:
    v = int(v)
    for i in range(mx-1, v-1, -1):
        dp[i] = min(dp[i-v]-w, dp[i])
ans = float('inf')
for i in range(C, mx):
    if dp[i]!=-1:
        ans = min(ans, dp[i]+make[i-C])
if ans == float('inf'):
    print('too poor')
else:
    print('{:.2f}'.format(ans))