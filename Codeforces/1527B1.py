import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().strip('\n')
    z = s.count('0')
    if z == 1:
        print('BOB')
        continue
    if z%2:
        print('ALICE')
    else:
        print('BOB')
