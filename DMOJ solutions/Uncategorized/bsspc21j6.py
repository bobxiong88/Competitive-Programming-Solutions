import sys
input = sys.stdin.readline
def dfs(node, p):
    r[node] = v[node]
    s = 0
    lol = []
    gay = 0
    for n in graph[node]:
        if n == p: continue
        dfs(n, node)
        r[node] += r[n]
        s += r[n]
        lol.append(r[n]-k[n])
        gay += k[n]
    if node != 1:
        if len(lol) > 2:
            lol.sort()
            k[node] = s-(lol[-2]+lol[-1])
        else:
            k[node] = gay
    else:
        if len(lol) > 3:
            lol.sort()
            k[node] = s-(lol[-3]+lol[-2]+lol[-1])
        else:
            k[node] = gay
N = int(input())
k = [0]*(N+1)
r = [0]*(N+1)
v = [0,0]+list(map(int,input().split()))
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1,1)
print(k[1])