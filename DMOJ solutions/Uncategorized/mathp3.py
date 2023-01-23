# 0 <= a[i+1]-a[i] <= 1
# 

import sys
input = sys.stdin.readline
N =int(input())
a = list(map(int,input().split()))
if a[0] != 1:
    print(-1)
    sys.exit(0)
curr = [a[0]]
group = []
for i in range(1,N):
    if not (0 <= a[i]-a[i-1] <= 1):
        print(-1)
        sys.exit(0)
    if a[i] != curr[-1]:
        group.append(curr)
        curr = []
    curr.append(a[i])
if curr: group.append(curr)
ans = []
cnt = 0
for g in group:
    for i in range(len(g)):
        ans.append(cnt+len(g)-i)
    cnt += len(g)
print(*ans)