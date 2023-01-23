def troll(lis,M):
    left = 0
    right = 0
    for a in lis:
        left+=M-a
        right+=a-1

    return max(left,right)
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
xs = []
ys = []
for i in range(N):
    x,y = map(int,input().split())
    xs.append(x)
    ys.append(y)
print(troll(xs,M)+troll(ys,M))