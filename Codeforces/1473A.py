import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    k = 0
    for i in a:
        if i>d:
            k+=1
    if k == 0:
        print('YES')
    else:
        a.sort()
        k=a[0]+a[1]
        if k<=d:
            print('YES')
        else:
            print('NO')
