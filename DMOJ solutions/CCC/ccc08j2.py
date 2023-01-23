import sys
p = list('ABCDE')
while True:
    b = int(input())
    n = int(input())
    for i in range(n):
        if b == 1:
            p.append(p[0])
            p = p[1:]
        elif b == 2:
            p.insert(0,p[-1])
            p = p[:5]
        elif b == 3:
            p[0], p[1] = p[1], p[0]
        else:
            print(*p)
            sys.exit(0)