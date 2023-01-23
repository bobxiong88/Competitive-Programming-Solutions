import sys
input = sys.stdin.readline
N, C = map(int,input().split())
pre = [0 for i in range(C+1)]
pre[0] = 1
for i in range(1,N+1):
    curr = [0 for i in range(C+1)]
    curr[0] = 1
    for j in range(1, C+1):
        v = 0
        if j-i >= 0:
            v = pre[j-i]
        curr[j] = curr[j-1]+pre[j]-v
        curr[j] %= int(1e9)+7
    pre = curr[:]
print(curr[C])