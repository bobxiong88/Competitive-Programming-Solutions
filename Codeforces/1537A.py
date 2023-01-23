import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    s = sum(a)
    if s/N < 1:
        print(1)
    elif s/N>1:
        print(s-N)
    else:
        print(0)
