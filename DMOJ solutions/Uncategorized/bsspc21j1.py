import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
k = (a+2)*3+16
if k <= b:
    print("Yes it fits!")
else:
    print("No, it's too small :(")