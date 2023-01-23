import sys
import math
input = sys.stdin.readline
a, n, p = map(int,input().split())
a%=p
m = math.ceil(math.sqrt(p))
v = dict()
for i in range(m, 0, -1):
    v[pow(a, i*m, p)] = i
ans = float('inf')
for j in range(m):
    curr = (pow(a, j, p)*n)%p
    if curr in v:
        res = v[curr]*m-j
        if  res < p:
            ans = min(ans, res)
if ans == float('inf'): ans = "DNE"
print(ans)