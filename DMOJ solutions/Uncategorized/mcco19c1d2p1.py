import sys
input = sys.stdin.readline
a = [0]*101
a[0] = 0
a[1] = 1
N = int(input())
for i in range(2, N+1):
    a[i] = a[i-1]*3-a[i-2]+2
print(a[N])