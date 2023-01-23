import sys
input = sys.stdin.readline
N = int(input())
T = int(input())
a = []
b = []
for i in range(N):
    xl, yt, xr, yb, t = map(int,input().split())
    a.append((xl, yt, yb, t))
    a.append((xr, yt, yb, -t))
    b.append(yt)
    b.append(yb)
a.sort()
b = list(b)
b.sort()
tint = [0 for i in range(len(b))]
ans = 0
b.append(10000000000000)
for i in range(len(a)-1):
    x1, ya, yb, v = a[i]
    x2, _, _, _ = a[i+1]
    for i in range(len(b)-1):
        if ya <= b[i] <= yb and ya <= b[i+1] <= yb:
            tint[i] += v
        if tint[i] >= T:
            ans += (x2-x1)*(b[i+1]-b[i])
print(ans)