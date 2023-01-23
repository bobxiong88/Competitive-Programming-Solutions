import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)
m = int(1e9)+7
def dfs(node, p):
    w = 1
    b = 1
    for n in graph[node]:
        if n == p: continue
        dfs(n, node)
        w*=(dw[n]+db[n])
        b*=dw[n]
        w%=m
        b%=m
    dw[node] = w
    db[node] = b
N = int(input())
graph = [[] for i in range(N+1)]
adj = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dw = [0 for i in range(N+1)]
db = [0 for i in range(N+1)]
dfs(1,-1)
print((dw[1]+db[1])%m)