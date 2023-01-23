import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(200000)
def top(node, visited, order):
    visited[node] = True
    for n in graph[node]:
        if node in graph[n]:
            print('inf')
            sys.exit(0)
        if not visited[n]:
            top(n, visited, order)
    order.append(node)
N, M = map(int,input().split())
graph = {}
for i in range(1,N+1):
    graph.update({i:{}})
for i in range(M):
    a,b = map(int,input().split())
    try:
        graph[a][b]+=1
    except:
        graph[a].update({b:1})
visited = [False]*(N+1)
order = []
top(1, visited, order)
order = list(reversed(order))
dp = [0]*(N+1)
dp[1] = 1

for node in order:
    for n in graph[node]:
        dp[n] += graph[node][n] * dp[node]
ans = str(dp[2])
if len(ans)>9:
    ans = ans[len(ans)-9:]
print(ans)