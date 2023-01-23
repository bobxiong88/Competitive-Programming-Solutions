import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    res = ['B' for i in range(m)]
    for i in a:
        x, y = i-1, m-i
        if x > y: x, y = y, x
        if res[x] == 'A':
            res[y] = 'A'
        else:
            res[x] = 'A'
    print(''.join(res))
