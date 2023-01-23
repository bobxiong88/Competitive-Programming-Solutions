import sys
input = sys.stdin.readline
def build():
    for i in range(n-1, 0, -1): t[i] = max(t[i<<1],t[i<<1|1])
def query(l, r):
    r+=1
    res = 0
    l += n
    r += n
    while l<r:
        if (l&1):
            res = max(res, t[l])
            l+=1
        if (r&1):
            r -= 1
            res = max(res, t[r])
        l>>=1
        r>>=1
    return res

N = int(input())
a = list(map(int,input().split()))
b = sorted(list(set(a)))
diff = []
ind = {}
for i in range(len(b)):
    ind[b[i]] = i
for i in range(len(b)-1):
    diff.append(b[i+1]-b[i])
n = len(diff)
t = [0]*(n*2+2)
for i in range(n):
    t[n+i] = diff[i]
build()
curr = 0
ans = 0
for i in range(N):
    if a[i] >= curr:
        curr = a[i]
    else:
        ans = max(ans, query(ind[a[i]], ind[curr]-1))
print(ans)