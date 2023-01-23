#solved this half a year ago... original sub too cursed, queue with regular array...
import sys
input = sys.stdin.readline
from collections import deque
K,N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,t,h = map(int,input().split())
    graph[a].append((b,t,h))
    graph[b].append((a,t,h))
A,B = map(int,input().split())
queue = deque([(A,0,K,-1)])
ans = []
distance = []
distance.append([float('inf')]*(N+1))
distance.append([-1]*(N+1))
distance[0][A] = 0
distance[1][A] = K
while queue:
    node, time, K, p = queue.popleft()
    for n,t,h in graph[node]:
        if n == p: continue
        if K-h>0 and not(time+t>=distance[0][n] and K-h<=distance[1][n]) :
            if time+t<distance[0][n]: distance[0][n] = time+t
            if K-h>distance[1][n]: distance[1][n] = K-h
            if n!=B:
                queue.append((n,time+t,K-h,node))
v = distance[0][B]
if v==float('inf'): v = -1
print(v)