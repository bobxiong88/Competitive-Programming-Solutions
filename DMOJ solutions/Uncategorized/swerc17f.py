import sys
input = sys.stdin.readline
W = int(input())
ans = 0
for _ in range(int(input())):
    w,l = map(int,input().split())
    ans += w*l
print(ans//W)