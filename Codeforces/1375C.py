import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    a = tuple(map(int,input().split()))
    if a[-1] > a[0]:
        print("YES")
    else:
        print("NO")
