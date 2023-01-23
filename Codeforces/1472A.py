import sys
input = sys.stdin.readline
for _ in range(int(input())):
    w,h,n = map(int,input().split())
    x = 1
    y = 1
    while w%2 == 0:
        x *= 2
        w /= 2
    while h%2 == 0:
        y *= 2
        h /= 2
    k = x*y
    if k >= n:
        print('YES')
    else:
        print('NO')
