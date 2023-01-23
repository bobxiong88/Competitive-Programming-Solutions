import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    a = []
    f = True
    for i in range(n):
        p,c = map(int,input().split())
        if c>p:
            f = False
        for x,y in a:
            if p<x:
                f = False
            if p==x and y!=c:
                f = False
            if c<y:
                f = False
            if c-y > p-x:
                f = False
        a.append((p,c))
    print('YES' if f else 'NO')
