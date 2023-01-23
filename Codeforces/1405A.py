import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    out = p[::-1]
    print(*out)
