import sys
input = sys.stdin.readline
a = int(input().strip('\n'), 16)
b = int(input().strip('\n'), 16)
if a+b > 1061109567:
    print("Yes")
else:
    print("No")