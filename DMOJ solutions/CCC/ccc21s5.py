import sys
input = sys.stdin.readline
def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)
def lcm(a, b):
    return a*b//gcd(a,b)
def build():
    for i in range(N-1, 0, -1):
        t[i] = gcd(t[i<<1],t[i<<1|1])
def query(l, r):
    r+=1
    res = ans[l]
    l += N
    r += N
    while l < r:
        if l&1:
            res = gcd(res, t[l])
            l += 1
        if r&1:
            r -= 1
            res = gcd(res, t[r])
        l >>= 1
        r >>= 1
    return res
N, M = map(int,input().split())
store = []
ans = [1]*N
t = [0]*(2*N)
freq = [[0 for i in range(17)] for i in range(N+1)]
for _ in range(M):
    x, y, z = map(int,input().split())
    x-=1
    y-=1
    freq[x][z] += 1
    freq[y+1][z] -= 1
    store.append((x,y,z))
for x in range(N):
    for i in range(17):
        if x: freq[x][i] += freq[x-1][i]
        if freq[x][i]: ans[x] = lcm(ans[x],i)
for i in range(N): t[N+i] = ans[i]
build()
for x, y, z in store:
    if query(x,y) != z:
        print("Impossible")
        sys.exit(0)
print(*ans)