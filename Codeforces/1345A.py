import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    if (n>1 and m>2) or (n>2 and m>1): print('NO')
    else: print('YES')
