import sys
input = sys.stdin.readline
sys.setrecursionlimit(120005)
def sqrt(n):
    return n**0.5
def dfs(node, p):
    global ans
    arr = []
    for n in adj[node]:
        if n == p: continue
        dfs(n, node)
        arr.append(dp[n])
        ans = max(ans, dp[n])
    if not val[node]:
        return
    dp[node] = 1
    arr.sort(reverse = True)
    if len(arr) == 0:
        ans = max(ans, 1)
    elif len(arr) == 1:
        dp[node] += arr[0]
    else:
        dp[node] += arr[0]
        ans = max(ans, arr[0]+arr[1]+1)
N = int(input())
val = [0]+[1 if (-1+sqrt(1+4*int(i)))/2 == int((-1+sqrt(1+4*int(i)))/2) else  0 for i in input().split()]
adj = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
ans = 0
dp = [0]*(N+1)
dfs(1,1)
print(max(ans,max(dp)))