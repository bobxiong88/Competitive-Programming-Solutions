import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
pre = [0,0]
for i in range(N):
    curr = [0,0]
    curr[0] = max(pre[1]+a[i], a[i])
    curr[1] = max(pre[0], pre[1])
    pre = curr[:]
print(max(curr))