import sys
input = sys.stdin.readline
N = int(input())
a = sorted(list(map(int,input().split())))
d = float('inf')
for i in range(N-1):
    d = min(d, a[i+1]-a[i])
print(d)