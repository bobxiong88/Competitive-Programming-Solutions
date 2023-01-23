import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = []
    if (n//2)%2:
        print('NO')
    else:
        print('YES')
        for i in range(1,n//2+1):
            a.append(i*2)
        for i in range(1,n//2):
            a.append(i*2-1)
        a.append(a[n//2-1]+n//2-1)
        print(*a)
