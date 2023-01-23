import sys
input = sys.stdin.readline
def dfs(node):
    vis[node] = True
    for n in graph[node]:
        if not vis[n]:
            dfs(n)
N, M, A, B = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
vis = [False for i in range(N+1)]
dfs(A)
if vis[B]:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")