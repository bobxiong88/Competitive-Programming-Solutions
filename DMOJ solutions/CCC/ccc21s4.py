import sys
input = sys.stdin.readline
from collections import deque
def update(p, v):
    p += n
    t[p] += v
    while p > 0:
        t[p>>1] = min(t[p], t[p^1])
        p >>= 1
def query(l, r):
    r+=1
    res = mx
    l += n
    r += n
    while l < r:
        if (l&1):
            res = min(res, t[l])
            l += 1
        if (r&1):
            r -= 1
            res = min(res, t[r])
        l >>= 1
        r >>= 1
    return res
N, W, D = map(int,input().split())
graph = [[] for i in range(N+1)]
mx = int(1e9)
n = int(2e5)+5
t = [0]*(2*n)
for i in range(W):
    a, b = map(int,input().split())
    graph[b].append(a)
queue = deque([(N, 0)])
dist = [mx]*(N+1)
dist[N] = 0
while queue:
    node, d = queue.popleft()
    if dist[node] < d:
        continue
    for v in graph[node]:
        if dist[v] > d + 1:
            dist[v] = d+1
            queue.append((v, d+1))
seq = [0]+list(map(int,input().split()))
for i in range(1, N+1):
    update(i, dist[seq[i]]+i-1)
for i in range(D):
    X, Y = map(int,input().split())
    a = seq[X]
    b = seq[Y]
    seq[X], seq[Y] = seq[Y], seq[X]
    update(X, -dist[a])
    update(Y, -dist[b])
    update(X, dist[b])
    update(Y, dist[a])
    print(query(1,N))