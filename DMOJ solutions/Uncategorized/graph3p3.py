import sys
input = sys.stdin.readline
def find(v):
    if parent[v] == v: return v
    parent[v] = find(parent[v])
    return parent[v]
def union(a,b):
    if size[a] < size[b]: a,b = b,a
    parent[b] = a
    size[a] += size[b]
n, m = list(map(int,input().split()))
a = []
b = []
for i in range(m):
    edge = tuple(map(int,input().split()))
    if edge[-1]: b.append(edge)
    else: a.append(edge)
a.sort(key = lambda x: x[2])
b.sort(key = lambda x: x[2])
edges = a+b
cost = 0
dan = 0
parent = [i for i in range(n+1)]
size = [0 for i in range(n+1)]
for a,b,c,d in edges:
    a,b = find(a),find(b)
    if find(a)!=find(b):
        if d: dan+=1
        union(a,b)
        cost += c
print dan, cost