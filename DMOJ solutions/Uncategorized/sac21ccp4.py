import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
pre = [0]*(N+1)
a = list(map(int,input().split()))
for i in range(1, N+1):
    pre[i] = pre[i-1]+a[i-1]
for i in range(Q):
    l,r = map(int,input().split())
    print(int((pre[r]-pre[l-1])/(r-l+1)))