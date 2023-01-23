import sys
input = sys.stdin.readline
def find(v):
    if v == parent[v]: return v
    parent[v] = find(parent[v])
    return parent[v]
def join(a,b):
    if a<b: a,b = b,a
    parent[b] = a
    size[a] += size[b]
n = int(input())
parent = [i for i in range(n)]
size = [1 for i in range(n)]
c = 0
for i in range(n):
    for j, x in enumerate(list(map(int,input().split()))):
        if x and j>i:
            a,b = find(i),find(j)
            if find(a)==find(b): c+=1
            else: join(a,b)
print(c)