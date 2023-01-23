import sys
input = sys.stdin.readline
M, N = map(int,input().split())
a = [int(input()) for i in range(N)]
a.sort()
l = 0
r = max(a)
use = 0
d = 0
#print(a)
while l <= r:
    m = (l+r)//2
    res = 0
    for i in range(N):
        res += max(0, a[i]-m)
    #print(m,res)
    if res <= M:
        use = res
        d = m
        r = m-1
    else:
        l = m+1
rem = M-use
ans = 0
for i in range(N-1,-1,-1):
    if d <= a[i]:
        a[i] = d
    if rem:
        if a[i]: a[i]-=1
        rem-=1
    #print(rem, a[i])
    ans += a[i]**2
print(ans%pow(2,63))