import sys
input = sys.stdin.readline
def check(x):
    hs = 0
    cnt = {}
    for i in range(x):
        hs += tb[x-i-1]*a[i]
        hs %= m
    cnt[hs] = 1
    for i in range(x,N):
        hs -= tb[x-1]*a[i-x]
        hs *= p
        hs += a[i]
        hs %= m
        if hs in cnt:
            cnt[hs] += 1
        else:
            cnt[hs] = 1
    res = 0
    for i in cnt:
        res = max(res, cnt[i])
    return res
N, K = map(int,input().split())
a = [int(input()) for i in range(N)]
p = 31
m = 5915587277
tb = [1]*(N+1)
for i in range(1,N+1):
    tb[i] = (tb[i-1]*p)%m
l = 1
r = N
ans = 0
while l<=r:
    mid = (l+r)//2
    if check(mid) >= K:
        ans = max(mid, ans)
        l = mid+1
    else:
        r = mid-1
print(ans)