import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    res = 0
    for x in range(n):
        if x == 0:
            print(0)
        else:
            print(x^(x-1))
        sys.stdout.flush()
        r = int(input())
        if r == 1:
            break
        
