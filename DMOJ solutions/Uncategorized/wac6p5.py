import sys
input = sys.stdin.readline
sys.setrecursionlimit(200005)
def dfs(node, p):
    child = []
    for n in graph[node]:
        if n == p: continue
        dfs(n, node)
        if not mark[n]:
            child.append(n)
        if len(child) == 2:
            mark[child[0]] = True
            mark[child[1]] = True
            print(child.pop(), child.pop())
    if child and p!=0:
        mark[node] = True
        mark[child[0]] = True
        print(p, child[0])
N = int(input())
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = []
mark = [False]*(N+1)
mark[0] = True
print(int((N-1)/2))
dfs(1,0)