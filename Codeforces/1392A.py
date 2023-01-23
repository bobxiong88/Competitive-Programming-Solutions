import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    p = True
    for i in a:
        if i != a[0]:
            p = False
            break
    if not p: print(1)
    else: print(n)
