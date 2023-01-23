import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = list(map(int,list(input().strip('\n'))))
    a = []
    for i in range(n):
        if i:
            x = a[i-1]+s[i-1]
            if x == 0:
                a.append(1)
            elif x == 1:
                if s[i] == 1:
                    a.append(1)
                else:
                    a.append(0)
            else:
                if s[i] == 0:
                    a.append(1)
                else:
                    a.append(0)
        else:
            a.append(1)
    print(''.join([str(i) for i in a]))
