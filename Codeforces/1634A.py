import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input().strip()
    if k == 0: print(1)
    elif s != s[::-1]: print(2)
    else: print(1)
