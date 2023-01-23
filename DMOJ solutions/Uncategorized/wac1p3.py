import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)
def dfs(node, ht):
    ht += 1
    for n in graph[node]:
        dfs(n, ht)
    if len(graph[node]) == 0:
        leaf.append((ht, node))
N, M, K = map(int,input().split())
graph = [[] for i in range(N+1)]
par = [i for i in range(N+1)]
a = [0,0]+list(map(int,input().split()))
vis = [False]*(N+1)
for i in range(2,N+1):
    graph[a[i]].append(i)
    par[i] = a[i]
leaf = []
dfs(1, 0)
leaf.sort(reverse = True)
res = [0]*(K+1)
for ht, n in leaf:
    curr = 0
    while not vis[n]:
        vis[n] = True
        curr += 1
        n = par[n]
    res.append(curr)
res.sort(reverse = True)
gay = res[:K]
tot = 0
while M>K:
    M-=K
    print(*gay, end = ' ')
print(*gay[:M])