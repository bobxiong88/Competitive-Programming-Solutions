import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    if n==1 and m == 1:
        print(0)
        continue
    if n > m: n,m = m,n
    print(n-1+m-1+n)
