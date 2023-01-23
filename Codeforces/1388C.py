import sys
from collections import deque
sys.setrecursionlimit(300000)
input = sys.stdin.readline
# what the pleas help
def dfs(node,pre):
    sub[node] = p[node]
    s = 0
    for n in graph[node]:
        if n!=pre:
            dfs(n, node)
            s += g[n]
            sub[node] += sub[n]
    if (sub[node]+h[node])%2!=0: poo[0] = False
    g[node] = (sub[node]+h[node])//2
    if not(g[node] >=0 and g[node] <= sub[node]): poo[0] = False
    if not s <= g[node]: poo[0] = False
for _ in range(int(input())):
    n,m = map(int,input().split())
    p = [0]+list(map(int,input().split()))
    h = [0]+list(map(int,input().split()))
    graph = [[] for i in range(n+1)]
    for i in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b); graph[b].append(a);
    sub = [0 for i in range(n+1)]
    g = [0 for i in range(n+1)]
    poo = [True]
    dfs(1,-1)
    print("YES" if poo[0] else "NO")
    
