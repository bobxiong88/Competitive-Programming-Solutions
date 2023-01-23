import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = list(map(int,input().split()))
    area = 0
    p = 0
    for i in range(3):
        x = i*2
        y = i*2+1
        area += a[x]*a[x-1]-a[y]*a[y-3]
        p += ((a[x]-a[x-2])**2+(a[y]-a[y-2])**2)**0.5
    print(abs(area/2), p)