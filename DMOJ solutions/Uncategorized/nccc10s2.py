import sys
input = sys.stdin.readline
from collections import deque
def top(node):
    vis[node] = True
    for n in g[node]:
        if not vis[n]:
            top(n)
    order.append(node)
N, K = map(int,input().split())
votes = [[ord(j)-ord('A') for j in input().strip()] for i in range(N)]
g = [[] for i in range(K)]
for i in range(K):
    for j in range(i):
        a = 0
        b = 0
        for x in votes:
            if x.index(i) < x.index(j):
                a += 1
            else:
                b += 1
            if a and b:
                break
        if a and not b:
            g[i].append(j)
        if b and not a:
            g[j].append(i)
order = []
vis = [False]*K
for i in range(K):
    top(i)
order = order[::-1]
dp = [1]*K
for i in order:
    for v in g[i]:
       dp[v] = max(dp[v], dp[i]+1)
print(max(dp))