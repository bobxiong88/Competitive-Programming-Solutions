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
N, R = map(int,input().split())
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
if max(counter)==0:
    print(0)
else:
    c = 0
    for bridge in bridges:
        u,v = bridge
        if counter[u]==1 or counter[v]==1:
            c+=1
    # i dont know what the fuck im even doing anymore
    v=0
    if max(counter)>1:
        v = counter.count(max(counter))
    print((c+1-v//2)//2)