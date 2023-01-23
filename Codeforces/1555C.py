import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    m = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sa = sum(a)
    sb = 0
    ans = float('inf')
    for i in range(m):
        sa -= a[i]
        if i>0:
            sb += b[i-1]
        #print(sa,sb)
        ans = min(ans, max(sa,sb))
    print(ans)
