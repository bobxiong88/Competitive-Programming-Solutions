import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = list(map(int,input().split()))
    a.sort()
    x,y,z = a
    if x**2+y**2 < z**2:
        print('O')
    elif x**2+y**2 > z**2:
        print('A')
    else:
        print('R')