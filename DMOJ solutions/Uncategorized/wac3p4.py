import sys
input = sys.stdin.readline
def find(v):
    if v == parent[v]: return v
    parent[v] = find(parent[v])
    return parent[v]
def union(a,b):
    a,b = find(a), find(b)
    if a!=b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
N, Q = map(int,input().split())
parent = [i for i in range(N+1)]
size = [1 for i in range(N+1)]
degree = [0 for i in range(N+1)]
odd, c = 0, 0
for i in range(Q):
    a,b,x = map(int,input().split())
    if degree[a] == 0: c+=1
    if degree[b] == 0: c+=1
    degree[a]+=x
    degree[b]+=x
    if (degree[a]-x)%2==0 and degree[a]%2: odd+=1
    if (degree[a]-x)%2 and degree[a]%2==0: odd-=1
    if (degree[b]-x)%2==0 and degree[b]%2: odd+=1
    if (degree[b]-x)%2 and degree[b]%2==0: odd-=1
    union(a,b)
    ans = "NO"
    if odd == 0 or odd == 2:
        if size[find(a)] == c:
            ans = "YES" 
    print(ans)