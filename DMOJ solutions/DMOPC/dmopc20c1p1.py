import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    s = input().strip('\n')
    a = 'C' in s
    b = 'M' in s
    if a and b:
        print("NEGATIVE MARKS")
    elif not a and not b:
        print("PASS")
    else:
        print("FAIL")