import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c = map(int,input().split())
    x = (a-1)+(c-1)
    y = abs(b-c)+(c-1)*2
    if x < y:
        print(1)
    elif x > y:
        print(2)
    else:
        print(3)
