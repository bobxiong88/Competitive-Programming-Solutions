import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a,b,n,m = map(int,input().split())
    small = min(a,b)
    large = max(a,b)
    if (small-m)<0:
        print("No")
        continue
    small-=m
    if (small+large-n)<0:
        print("No")
        continue
    print("Yes")
