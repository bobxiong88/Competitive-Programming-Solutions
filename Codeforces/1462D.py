import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    pos = []
    for i in range(1,n+1):
        if s % i == 0:
            pos.append(s // i)
    pos = pos[::-1]
    for x in pos:
        new = []
        c = 0
        gay = True
        for i in range(n):
            c += a[i]
            if c == x:
                new.append(s)
                c = 0
            if c > x:
                gay = False
                break
        if gay:
            print(n-s // x)
            break
        
