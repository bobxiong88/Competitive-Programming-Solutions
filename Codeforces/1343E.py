import sys
input = sys.stdin.readline
from collections import deque
def bfs(node):
    dist = [float('inf')]*(len(graph)+1)
    queue = deque([node])
    dist[node] = 0
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if dist[n] > dist[node]+1:
                dist[n] = dist[node]+1
                queue.append(n)
    return dist
for _ in range(int(input())):
    n,m,a,b,c = map(int,input().split())
    p = list(map(int,input().split()))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    da = bfs(a)
    db = bfs(b)
    dc = bfs(c)
    ans = float('inf')
    p.sort()
    pre = [0]
    for i in p: pre.append(pre[-1]+i)
    for i in range(1, n+1):
        d1, d2, d3 = da[i], db[i], dc[i]
        if d1+d2+d3 > m: continue
        ans = min(pre[d1+d2+d3]+pre[d2],ans)
    print(ans)
        
    
