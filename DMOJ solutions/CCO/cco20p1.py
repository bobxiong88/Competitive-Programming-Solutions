import sys
input = sys.stdin.readline
from math import floor
N = int(input())
L, R, Y = map(int,input().split())
sweep = []
layer = 0
for i in range(N):
    x, v, h = map(int,input().split())
    a = x-h*Y/v
    b = x+h*Y/v
    if floor(a) == a:
        a = int(a)+1
    else:
        a = floor(a)+1
    if floor(b) == b:
        b = int(b)
    else:
        b = floor(b)+1
    if a <= L:
        layer += 1
    else:
        sweep.append((a,1))
    sweep.append((b,-1))
sweep.append((R+1,0))
sweep.sort()
last = L
ans = [0]*(N+1)
for x, v in sweep:
    ans[layer] += x-last
    layer += v
    last = x
    if x == R+1:
        break
for i in range(N+1):
    if i:
        ans[i] += ans[i-1]
    print(ans[i])