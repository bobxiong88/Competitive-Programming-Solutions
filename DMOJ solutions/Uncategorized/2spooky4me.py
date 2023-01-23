import sys
input = sys.stdin.readline
N, L, S = map(int,input().split())
points = [(L+1, 0)]
prev = 1
curr = 0
for i in range(N):
    a, b, s = map(int,input().split())
    points.append((a, s))
    points.append((b+1, -s))
points.sort()
ans = 0
for p, x in points:
    if curr < S:
        ans += p-prev
    prev = p
    curr += x
print(ans)