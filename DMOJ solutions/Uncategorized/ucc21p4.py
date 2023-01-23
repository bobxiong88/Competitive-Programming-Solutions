import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
dist = [float('inf')]*(N+1)
m = 2021
fib = [0]*(N+1)
fib[1] = 1
a = [0]*(N+1)
a[1] = 2
for i in range(2,N+1):
    fib[i] = fib[i-1]+fib[i-2]
    fib[i] %= m
    a[i] = fib[i]+i%50
dist[1] = 0
queue = deque([(1, 0)])
while queue:
    node, d = queue.popleft()
    if d > dist[node]: continue
    p = [node+a[node],node-a[node],node+1,node-1]
    for n in p:
        if 1 <= n <=N:
            if d+1 < dist[n]:
                dist[n] = d+1
                queue.append((n,d+1))
print(dist[N])