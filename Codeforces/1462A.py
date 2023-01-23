import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    x = [0 for i in range(n)]
    for i in range(n):
        if i%2 == 0:
            x[i] = a[i//2]
        else:
            x[i] = a[~(i//2)]
    print(*x)
