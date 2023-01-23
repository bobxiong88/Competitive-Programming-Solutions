import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000005)
def find(a):
    if par[a] == a: return a
    par[a] = find(par[a])
    return find(par[a])
def join(a,b):
    a,b = find(a),find(b)
    if a == b: return
    #if sz[a] < sz[b]: a,b = b,a
    par[b] = a
    sz[a] += sz[b]
N, M = map(int,input().split())
par = [i for i in range(N+1)]
sz = [1 for i in range(N+1)]
for i in range(M):
    line = list(map(int,input().split()))
    if len(line) <= 1: continue
    for i in line[1:]:
        join(i,line[1])
ans = []
for i in range(1,N+1):
    if find(1) == find(i):
        ans.append(i)
print(len(ans))
print(*ans)