import sys
input = sys.stdin.readline
n = int(input()); m = int(input())
graph = [dict() for i in range(n+1)]
cnt = [0]*(n+1)
edges = dict()
for i in range(m):
    a,b = map(int,input().split())
    cnt[a]+=1
    cnt[b]+=1
    if b in graph[a]:
        graph[a][b] += 1
    else:
        graph[a][b] = 1
    if a in graph[b]:
        graph[b][a] += 1
    else:
        graph[b][a] = 1
    k = tuple(sorted([a,b]))
    if k in edges: edges[k]+=1
    else: edges[k] = 1
c = 0
h = 0
ans = 0
t = [-1]*(n+1)
for a in range(1, n+1):
    if cnt[a] == 4:
        t[a] = 0
    elif cnt[a] == 1:
        t[a] = 1
    else:
        print("Impossible")
        sys.exit(0)
for edge in edges:
    a,b = edge
    if edges[edge] == 1:
        if sorted([t[a],t[b]]) == [0,1]:
            ans += 413
        elif sorted([t[a],t[b]]) == [0,0]:
            ans += 346
        else:
            print("Impossible")
            sys.exit(0)
    elif edges[edge] == 2:
        if sorted([t[a],t[b]]) == [0,0]:
            ans += 615
        else:
            print("Impossible")
            sys.exit(0)
    else:
        print("Impossible")
        sys.exit(0)
out = ''
if t.count(0) == 1:
    out += 'C'
else:
    out += 'C{}'.format(t.count(0))
if t.count(1) == 1:
    out += 'H'
else:
    out += 'H{}'.format(t.count(1))
print(ans)
print(out)