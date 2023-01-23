import sys
input = sys.stdin.readline
n,k,t = map(int,input().split())
if k<=t<=n:
    print(k)
else:
    print(min(t,abs(n+k-t)))
