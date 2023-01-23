import sys
input = sys.stdin.readline
n, q = map(int,input().split())
k = list(map(int,input().split()))
pre = [0]
for i in range(n):
    pre.append(pre[i]+k[i])
for i in range(q):
    a,b = map(int,input().split())
    print(pre[n]-(pre[b]-pre[a-1]))