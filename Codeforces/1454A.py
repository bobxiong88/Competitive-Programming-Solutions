import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = [i for i in range(1,n)]
    a = [n]+a
    print(*a)
