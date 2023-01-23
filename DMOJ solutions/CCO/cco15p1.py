import sys
input = sys.stdin.readline
from math import ceil
n, w = map(int,input().split())
a = [int(input()) for i in range(n)]
a.sort()
if w < a[0]:
    mn = a[-1]-w
elif w > a[-1]:
    mn = w-a[0]
else:
    mn = a[-1]-a[0]
mx1 = abs(a[0]-w)
for i in range(n//2):
    mx1 += max(abs(a[i]-a[n-i-1]), abs(a[n-i-1]-w))
    if i != n//2-1 or n%2:
        mx1 += max(abs(a[n-i-1]-a[i+1]), abs(a[i+1]-w))
a = a[::-1]
mx2 = abs(a[0]-w)
for i in range(n//2):
    mx2 += max(abs(a[i]-a[n-i-1]), abs(a[n-i-1]-w))
    if i != n//2-1 or n%2:
        mx2 += max(abs(a[n-i-1]-a[i+1]), abs(a[i+1]-w))
print(mn, max(mx1,mx2))