import sys
input = sys.stdin.readline
def find(v):
    if parent[v] == v: return v
    parent[v] = find(parent[v])
    return parent[v]
def join(a,b):
    if size[a] < size[b]: a,b = b,a
    size[a] += size[b]
    parent[b] = a
def dist(x1,x2,y1,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input())
parent = [i for i in range(n+1)]
size = [1 for i in range(n+1)]
nodes = [0]+[tuple(map(int,input().split())) for i in range(n)]
m = int(input())
c = 0
for i in range(m):
    a,b = map(int,input().split())
    a,b = find(a),find(b)
    if a!=b:
        c+=1
        join(a,b)
edges = []
for i in range(1,n+1):
    x1,y1 = nodes[i]
    for j in range(i+1,n+1):
        x2,y2 = nodes[j]
        edges.append((i,j,dist(x1,x2,y1,y2)))
edges.sort(key = lambda x: x[2])
ans = 0
add = []
for i,j,w in edges:
    if c>=n-1: break
    a,b = find(i),find(j)
    if a != b:
        c+=1
        ans += w
        add.append((i,j))
        join(a,b)
ans = round(ans,2)
if ans == 0: print('0.00')
else:print(round(ans,2))
for a,b in add: print a,b