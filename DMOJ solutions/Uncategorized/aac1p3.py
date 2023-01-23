import sys
input = sys.stdin.readline
N, X = map(int,input().split())
a = [0]*N
if (N-X) % 2:
    print(-1)
else:
    for i in range(0, N-X, 2):
        a[i] = 1
    print(*a)