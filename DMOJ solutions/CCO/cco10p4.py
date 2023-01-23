import sys
input = sys.stdin.readline
T = int(input())
N = int(input())
comp = [[0 for i in range(3005)] for i in range(T)]
for i in range(N):
    c,v,t = map(int,input().split())
    comp[t-1][c] = max(comp[t-1][c], v)
B = int(input())
for i in range(T):
    for j in range(1,B+1):
        comp[i][j] = max(comp[i][j], comp[i][j-1])
curr = comp[0][:]
for i in range(1,T):
    dp = [0 for i in range(3005)]
    for x in range(1,B+1):
        for y in range(1,B+1-x):
            dp[x+y] = max(curr[x]+comp[i][y], dp[x+y])
    curr = dp[:]
print(curr[B])