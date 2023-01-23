import sys
from heapq import *
from collections import deque
input = sys.stdin.readline
N = int(input())
city = [tuple(map(int,input().split())) for i in range(N)]
adj = [[0 for j in range(N)] for i in range(N)]
X = int(input())-1
for i in range(N):
    x1, y1 = city[i]
    for j in range(N):
        if i == j: continue
        x2, y2 = city[j]
        dist = (x1-x2)**2+(y1-y2)**2
        adj[i][j] = dist
        adj[j][i] = dist
dist = [float('inf') for i in range(N)]
dist[X] = 0
u = [False]*(N)
for i in range(N):
    v = -1
    for j in range(N):
        if not u[j] and (v == -1 or dist[j] < dist[v]):
            v = j
    if dist[v] == float('inf'):
        break
    u[v] = True
    for n, w in enumerate(adj[v]):
        if dist[v] + w < dist[n]:
            dist[n] = dist[v]+w

dist.sort()
for i in range(int(input())):
    q = int(input())
    res = 0
    if q == 0:
        print(1)
        continue
    if q >= dist[-1]:
        print(N)
        continue
    l = 0
    r = N-1
    while l<=r:
        m = (l+r)//2
        if dist[m] <= q < dist[m+1]:
            res = m+1
            break
        if dist[m] > q:
            r = m-1
        else:
            l = m+1
    print(res)