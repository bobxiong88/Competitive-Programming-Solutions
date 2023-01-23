import sys
input = sys.stdin.readline
N = int(input())
a = [1,2,3]
for i in range(3,N):
    a.append((1+a[i-1]+a[i-3])%(int(1e9)+7))
print(a[N-1])