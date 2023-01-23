import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    if n<4:
        print(-1)
        continue
    if n==4:
        print(2,4,1,3)
        continue
    a = []
    if n%2:
        for i in range(1,n//2+2):
            a.append(i*2-1)
        a.append(n-3)
        a.append(n-1)
        for i in range(n-5,0,-2):
            a.append(i)
    else:
        for i in range(1,n//2+1):
            a.append(i*2-1)
        a.append(n-4)
        a.append(n)
        a.append(n-2)
        for i in range(n-6,0,-2):
            a.append(i)
        
    print(*a)
