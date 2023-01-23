import sys
input = sys.stdin.readline
N, R, S = map(int,input().split())
dp = [[[0,-1] for i in range(S+1)] for j in range(R+1)]
d = []
for x in range(N):
    E, V, A, B = input().split()
    V, A, B = int(V), int(A), int(B)
    d.append((E, V, A, B))
    for i in range(A,R+1):
        for j in range(B,S+1):
            if dp[i][j][0] < V+dp[i-A][j-B][0]:
                dp[i][j][0] = V+dp[i-A][j-B][0]
                dp[i][j][1] = x
mx = dp[R][S][0]
count = [0 for i in range(N)]
while R>0 and S>0:
    _,x = dp[R][S]
    if x == -1: break
    E, V, A, B = d[x]
    count[x] += 1
    R-=A
    S-=B
print(mx)
for i in range(N):
    print('{} {}'.format(d[i][0], count[i]))