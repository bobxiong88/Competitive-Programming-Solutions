import sys
input = sys.stdin.readline
from collections import deque
def bfs(A, B, graph):
    queue = deque([(A, 0)])
    dist = [float('inf')]*(N+1)
    dist[A] = 0
    while queue:
        node, d = queue.popleft()
        if d > dist[node]: continue
        for n, w in graph[node]:
            if d+w < dist[n]:
                dist[n] = d+w
                queue.append((n, d+w))
    return dist
def bs(D):
    l = 0
    r = M-1
    if D<edge[l][0]:
        return -1
    if edge[r][0] <= D:
        return M-1
    while l <= r:
        m = (l+r)//2
        if edge[m][0] <= D < edge[m+1][0]:
            return m
        if edge[m][0] <= D:
            l = m+1
        else:
            r = m-1
N, M, A, B = map(int,input().split())
adj, rev = [[[] for i in range(N+1)] for j in range(2)]
temp = []
edge = []
psa = [0]*M
for i in range(M):
    x, y, l, c = map(int,input().split())
    adj[x].append((y, l))
    rev[y].append((x, l))
    temp.append((x,y,l,c))
go = bfs(A, B, adj)
back = bfs(B, A, rev)
for x, y, l, c in temp:
    d = go[x] + l + back[y]
    edge.append((d, c))
edge.sort()
for i in range(M):
    psa[i] = edge[i][1]
    if i: psa[i] += psa[i-1]
Q = int(input())
for i in range(Q):
    D = int(input())
    x = bs(D)
    
    if x == -1:
        res = 0
    else:
        res = psa[x]
    print(res)