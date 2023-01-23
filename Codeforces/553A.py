import sys
input = sys.stdin.readline
n = 1005
mod = int(1e9)+7
pre = [[0 for i in range(n)] for j in range(n)]
pre[0][0] = 1
for i in range(1,n):
    for j in range(n):
        pre[i][j] = pre[i-1][j-1] + pre[i-1][j]
        pre[i][j]%=mod
k = int(input())
s = 0
ans = 1
for i in range(k):
    c = int(input())
    s += c
    #print(s,c)
    ans *= pre[s-1][c-1]
    ans%=mod
print(ans%mod)
