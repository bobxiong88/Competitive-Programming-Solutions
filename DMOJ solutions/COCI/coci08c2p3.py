import sys
N = int(input())
a = [tuple(map(int,input().split())) for i in range(N)]
i = 0
ans = float('inf')
while i < (1 << N):
    s = 0
    m = 1
    for j in range(N):
        if i&1 << j:
            s += a[j][1]
            m *= a[j][0]
    if i: ans = min(ans, abs(s-m))
    i += 1
print(ans)