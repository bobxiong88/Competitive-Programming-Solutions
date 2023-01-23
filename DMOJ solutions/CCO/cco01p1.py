import sys
from collections import deque
input = sys.stdin.readline
def gcd(a,b):
    if a == 0: return b
    return gcd(b%a, a)
def lcm(a,b):
    return a*b//gcd(a,b)
while True:
    n = int(input())
    if not n: break
    graph = [[] for i in range(n+1)]
    for i in range(n):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    vis = [False]*(n+1)
    ans = 1
    for i in range(1,n+1):
        if not vis[i]:
            c = 0
            queue = deque([i])
            vis[i] = True
            while queue:
                c+=1
                node = queue.popleft()
                for v in graph[node]:
                    if not vis[v]:
                        vis[v] = True
                        queue.append(v)
            ans = lcm(ans, c)
    print(ans)