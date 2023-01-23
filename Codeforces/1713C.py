# always possible
from math import *
import sys
input = sys.stdin.readline
def solve(n, k):
    if n == 0:
        return
    if n == 1:
        ans[0] = 0
        return
    if n == 2:
        ans[0] = 1
        ans[1] = 0
        return
    if n == 5:
        ans[0] = 4
        ans[1] = 3
        ans[2] = 2
        ans[3] = 1
        ans[4] = 0
        return
    z = ceil(sqrt(n))**2
    x = 0
    for i in range(z-n+1, n):
        ans[k-x] = i
        x += 1
    #print(n,k,z,ans)
    solve(n-(2*n-z-1), k-(2*n-z-1))
for _ in range(int(input())):
    n = int(input())
    ans = [0]*n
    solve(n, n-1)
    print(*ans)
