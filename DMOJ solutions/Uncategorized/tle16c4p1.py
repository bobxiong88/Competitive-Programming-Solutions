import sys
input = sys.stdin.readline
N = int(input())
a = [int(input()) for i in range(N)]
a.sort()
ans = 0
s = 0
for i in range(N):
    if a[i] >= s:
        s += a[i]
        ans += 1
print(ans)