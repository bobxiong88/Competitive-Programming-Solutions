import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a,b,c = arr[0], arr[1], arr[-1]
    if a+b>c:
        print(-1)
    else:
        print(1,2,n)
