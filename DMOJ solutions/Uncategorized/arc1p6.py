# find p[X][A] and p[A][Y] such that
# p[X][A].val+p[A][Y].val-union(p[X][A], p[A][Y])
# is minimized
# once A is reached
# 1. go forward, then its just the minimum distance form A to Y
# 2. background, minimum distance from some point on the path p[X][A] to Y
# for any particular path p[X][A], the best answer is just the length of
# path p[X][A]+minimum from some point on p[X][A] to Y
# cost[X] = min path from some point X to Y
# ans[A] = [min path here, best ans]
# push min(min path+cost[A]+a[A], best ans+a[A]) --> next one
import sys
from heapq import *
input = sys.stdin.readline

N, M, X, Y, Q = map(int,input().split())
a = [0]+list(map(int,input().split()))
g = [[] for i in range(N+1)]
for i in range(M):
    u, v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
cost = [float('inf')]*(N+1)
cost[Y] = a[Y]
queue = [(a[Y], Y)]
heapify(queue)
while queue:
    d, u = heappop(queue)
    if d > cost[u]: continue
    for v in g[u]:
        if cost[v] > d+a[v]:
            cost[v] = d+a[v]
            heappush(queue, (cost[v], v))
ans = [[float('inf'), float('inf')] for i in range(N+1)]
ans[X] = [a[X], cost[X]]
queue = [(cost[X], X)]
heapify(queue)
while queue:
    bst, u = heappop(queue)
    if bst > ans[u][1]: continue
    for v in g[u]:
        pushVal = min(ans[u][1]+a[v], ans[u][0]+cost[v])
        if ans[v][0] > ans[u][0]+a[v] or ans[v][1] > pushVal:
            ans[v][0] = min(ans[u][0]+a[v], ans[v][0])
            ans[v][1] = min(ans[v][1], pushVal)
            #queue.append((ans[v][1],v))
            heappush(queue,(ans[v][1],v))
sys.stdout.write('\n'.join([str(ans[int(input())][1]) for i in range(Q)]))