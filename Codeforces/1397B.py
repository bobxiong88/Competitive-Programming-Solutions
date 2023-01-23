import sys
input = sys.stdin.readline
from math import log
n = int(input())
a = list(map(int,input().split()))
a.sort()
mx = 1
while (mx)**(n-1) <= 1e9: mx+=1
if mx**(n-1)>1e20: mx = 1
ans = float('inf')
for i in range(1, mx+1):
    mn = 0
    p = 1
    for j in a:
        mn+=abs(p-j)
        p*=i
    ans=min(ans,mn)
print(ans)
