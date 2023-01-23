import sys
input = sys.stdin.readline
W = int(input())
N = int(input())
a = [int(input()) for i in range(N)]
s = 0
for i in range(N):
    s += a[i]
    if i - 4 >= 0:
        s -= a[i-4]
    if s > W:
        break
print(i+int(s <= W))