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
graph = {}
while True:
    a,b,_ = list(input())
    if a=="*":
        break
    try:
        graph[a].append(b)
    except:
        graph.update({a:[b]})
    try:
        graph[b].append(a)
    except:
        graph.update({b:[a]})
bridges = []
low = {}
pre = {}
count = 0
counter = {}
for key in graph:
    low.update({key:-1})
    pre.update({key:-1})
    counter.update({key:0})
for key in graph:
    if pre[key] == -1:
        dfs('A','B',count)
for b in bridges:
    print(''.join(sorted(b)))
print "There are",len(bridges),"disconnecting roads."