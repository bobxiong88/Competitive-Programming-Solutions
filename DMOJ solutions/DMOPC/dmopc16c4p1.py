import sys
input = sys.stdin.readline
a = set()
for i in range(64):
    a.add(2**i)
n = int(input())
for i in range(n):
    x = int(input())
    if x in a:
        print('T')
    else:
        print('F')