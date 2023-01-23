import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m,r,c = map(int,input().split())
    print(max(abs(n-r),abs(1-r))+max(abs(m-c), abs(1-c)))
