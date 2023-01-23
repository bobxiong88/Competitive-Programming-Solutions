import sys
input = sys.stdin.readline
x, y = map(int,input().split())
print("{}.{}".format(x*y//2, '5' if (x*y)%2 else '0'))