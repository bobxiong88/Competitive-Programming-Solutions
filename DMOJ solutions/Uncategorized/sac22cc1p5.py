import sys
input = sys.stdin.readline
N, K = map(int,input().split())
c = [-float('inf')]+list(map(int,input().split()))
h = [-float('inf')]+list(map(int,input().split()))
if K >= N:
    print(0)
    sys.exit(0)
dp = [[float('inf')]*(K+1) for i in range(N+1)]
for x in range(K+1):
    dp[0][x] = 0
gamer = [[float('inf')]*(N+1) for j in range(N+1)]
for i in range(1,N+1):
    curr = []
    for j in range(i,N+1):
        curr.append((h[j],c[j]))
        curr.sort()
        for x, _ in curr:
            dab = 0
            for a, b in curr:
                dab += abs(a-x)*b
            gamer[i][j] = min(dab,gamer[i][j])
s = 0
for i in range(1,N+1):
    s += c[i]*h[i]
    dp[i][0] = s
    for x in range(1,K+1):
        for j in range(i):
            dp[i][x] = min(dp[j][x-1]+gamer[j+1][i],dp[i][x])
print(dp[N][K])