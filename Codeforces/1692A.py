import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    b,c,d = sorted([b,c,d])
    if a > d: print(0)
    elif a > c: print(1)
    elif a > b: print(2)
    else: print(3)
