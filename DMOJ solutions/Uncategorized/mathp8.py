import sys
input = sys.stdin.readline
def get(N, K, curr):
    if K == 0:
        res.add(tuple(curr))
        return
    for i in range(N-1):
        new = curr[:]
        new[i],new[i+1] = new[i+1],new[i]
        get(N, K-1, new)
N, K = map(int,input().split())
'''
for i in range(2,N+1):
    row = []
    for j in range(K+1):
        res = set()
        get(i,j,[x for x in range(1,i+1)])
        row.append(len(res))
    print(row)
mx = 15
'''
m = int(1e9)+7
dp = [[1 for i in range(3005)] for j in range(3005)]
for i in range(1,N-1):
    k = 0
    for j in range(1,K+1):
        top = dp[i-1][j]
        if j>=i+2:
            top -= dp[i-1][k]
            k += 1
        dp[i][j] = (dp[i][j-1]+top)%m
print(dp[N-2][K])