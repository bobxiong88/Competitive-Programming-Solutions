import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    g0 = []
    for i in range(n):
        g0.append(input())
    r1 = []
    r2 = []
    for i in range(m):
        if i%2:
            r1.append('W')
            r2.append('R')
        else:
            r1.append('R')
            r2.append('W')
    g1 = []
    g2 = []
    for i in range(n):
        if i%2:
            g1.append(r1)
            g2.append(r2)
        else:
            g1.append(r2)
            g2.append(r1)
    p = [True, True]
    for i in range(n):
        for j in range(m):
            if g0[i][j] == 'R' and g1[i][j] == 'W':
                p[0] = False
            if g0[i][j] == 'W' and g1[i][j] == 'R':
                p[0] = False
            if g0[i][j] == 'R' and g2[i][j] == 'W':
                p[1] = False
            if g0[i][j] == 'W' and g2[i][j] == 'R':
                p[1] = False
    if any(p):
        print("YES")
        if p[0]:
            for i in range(n):
                print(''.join(g1[i]))
        else:
            for i in range(n):
                print(''.join(g2[i]))
    else:
        print("NO")

            
