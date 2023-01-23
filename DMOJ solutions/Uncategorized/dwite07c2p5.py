import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(200000)
def dfs(u, v, count):
    pre[v] = count
    low[v] = pre[v]
    count+=1
    for w in graph[v]:
        if pre[w] == -1:
            dfs(v,w,count)
            low[v] = min(low[v], low[w])
            if low[w] == pre[w]:
                bridges.append((v,w))
                counter[v]+=1
                counter[w]+=1
        elif w!=u:
            low[v] = min(low[v], pre[w])
for i in range(5):
    N = int(input())
    R = int(input())
    graph = [[]for i in range(N+1)]
    for i in range(R):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    low = [-1]*(N+1)
    pre = [-1]*(N+1)
    bridges = []
    count = 0
    counter = [0]*(N+1)
    for node in range(1, N+1):
        if pre[node] == -1:
            dfs(node, node, count)
    print(len(bridges))