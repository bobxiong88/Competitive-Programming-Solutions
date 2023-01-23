import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    d = k*(n/(n-1))
    if d == int(d):
        print(int(d-1))
    else:
        print(int(d))
