import sys
input = sys.stdin.readline
def dfs(node):
    curr.append((a[node],node))
    for v in graph[node]:
        if not vis[v]:
            vis[v] = True
            dfs(v)        
for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    p = list(map(int,input().split()))
    graph = [[] for i in range(n)]
    for i in p:
        i-=1
        graph[i+1].append(i)
        graph[i].append(i+1)
    vis = [False]*n
    new = [0]*n
    for i in range(n):
        if vis[i]:continue
        vis[i] = True
        curr = []
        dfs(i)
        curr.sort()
        pos = []
        for _,b in curr:
            pos.append(b)
        pos.sort()
        for i in range(len(curr)):
            new[pos[i]] = curr[i][0]
    if new == sorted(a):print('YES')
    else:print('NO')
