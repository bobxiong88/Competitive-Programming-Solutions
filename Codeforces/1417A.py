import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    m = a[0]
    c = 0
    for i in range(1,n):
        c += (k-a[i])//m
    print(c)
