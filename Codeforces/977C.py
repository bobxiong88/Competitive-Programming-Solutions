import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
c = 0
if not k:
    if a[0]<=1: print(-1)
    else: print(1)
    sys.exit(0)
ans = a[k-1]
for i in a:
    if i<=ans: c+=1
if c>k: print(-1)
else: print(ans)
