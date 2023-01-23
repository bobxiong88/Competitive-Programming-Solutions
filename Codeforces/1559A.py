import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = a[0]
    for i in range(n):
        res &= a[i]
    print(res)
