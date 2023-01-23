import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, x = map(int,input().split())
    a = (x-1)//n+1 # col
    b = (x-1)%n+1# row
    print((b-1)*m+a)
