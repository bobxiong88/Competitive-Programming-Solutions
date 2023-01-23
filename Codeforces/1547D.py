import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]
    for i in range(1,n):
        if a[i-1]&a[i] == a[i-1]:
            b.append(0)
        else:
            x = a[i-1]
            y = a[i]
            z = 0
            for j in range(30):
                if x&1 and not (y&1):
                    z += pow(2, j)
                y>>=1
                x>>=1
            b.append(z)
        a[i] ^= b[i]
    print(*b)
