import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
ans = 0
mx = a[0]
m = int(1e9)+7
s = 0
for i in range(N):
    if a[i] >= mx:
        ans = (s + 1)%m
    s = (s+ans)%m
    mx = max(a[i],mx)
print(ans)