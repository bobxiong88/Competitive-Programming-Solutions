import sys
input = sys.stdin.readline
for _ in range(int(input())):
    h = int(input())
    a = h//3
    b = (h-a)//2
    c = h-b-a
    print(a*b*c)