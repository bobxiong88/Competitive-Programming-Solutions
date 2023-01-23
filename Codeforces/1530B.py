import sys
input = sys.stdin.readline
for _ in range(int(input())):
    h, w = map(int,input().split())
    
    pos = []
    for i in range(w):
        pos.append((0, i))
    for i in range(1,h-1):
        pos.append((i, w-1))
    for i in range(w-1, -1, -1):
        pos.append((h-1, i))
    for i in range(h-2, 0, -1):
        pos.append((i,0))
    ans = 0
    for i in range(len(pos)):
        res = 0
        t = [[0]*w for i in range(h)]
        for x, y in pos:
            p = True
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0: continue
                    a = i+x
                    b = j+y
                    if 0<=a < h and 0 <= b < w:
                        if t[a][b]:
                            p = False
            if p:
                t[x][y] = 1
                res += 1
        if res > ans:
            ans = res
            tf = [i[:] for i in t]
    for i in tf:
        print(''.join([str(j) for j in i]))
    print()
