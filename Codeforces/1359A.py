import sys
input = sys.stdin.readline
def ceil(a, b):
    return -(-a // b)
t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    j1 = min(m,n//k)
    left = m-j1
    j2 = ceil(left,k-1)
    print(j1-j2)
