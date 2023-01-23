import sys
input = sys.stdin.readline
def find(v):
    if v == par[v]: return v
    par[v] = find(par[v])
    return par[v]
def join(a,b):
    a = find(a)
    b = find(b)
    if a == b: return
    if sz[a] < sz[b]: a, b = b, a
    sz[a] += sz[b]
    par[b] = a
for  _ in range(int(input())):
    N = int(input())
    a = [[],[]]
    a[0] = list(map(int,input().split()))
    a[1] = list(map(int,input().split()))
    par = [i for i in range(2*N+2)]
    sz = [1 for i in range(2*N+2)]
    for i in range(N):
        join(a[0][i],a[0][i]+N)
        join(a[0][i],a[1][i]+N)
    comp = set()
    for i in range(1,2*N+1):
        comp.add(find(i))
    m = int(1e9)+7
    print(pow(2,len(comp),m))
        
