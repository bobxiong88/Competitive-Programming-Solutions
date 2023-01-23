import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
for i in range(N):
    if a[i]%2:
        a[i] = -1000000000000
s = 0
ans = 0
for i in range(N):
    s += a[i]
    if s < 0:
        s = 0
    ans = max(s,ans)
print(ans)