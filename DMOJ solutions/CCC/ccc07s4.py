import sys
input = sys.stdin.readline
n = int(input())
graph = {}
for i in range(1,n+1):
    graph.update({i:[]})
while True:
    a,b = map(int,input().split())
    if (a,b) == (0,0):
        break
    graph[a].append(b)
dp = [0]*(n+1)
dp[1] = 1
for i in range(1,n+1):
    for node in graph[i]:
        dp[node]+=dp[i]
print(dp[n])