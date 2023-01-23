import sys
input = sys.stdin.readline
a = sum([int(input()) for i in range(6)])/6
a += int(input())
if a >= int(input()):
    print("yes")
else:
    print("no")