# say you 

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = [int(i) for i in input().strip('\n')]
    n = len(s)
    gp = []
    curr = s[0]
    cnt = 0
    for i in range(n):
        if s[i] != curr:
            gp.append((curr, cnt))
            curr = s[i]
            cnt = 0
        cnt += 1
    gp.append((curr,cnt))
    m = len(gp)
    smin = [9]*(m+1)
    for i in range(m-1, -1, -1):
        smin[i] = min(smin[i+1], gp[i][0])
    bad = []
    good = []
    for i in range(m):
        if gp[i][0] > smin[i]:
            bad.append((min(gp[i][0]+1, 9), gp[i][1]))
        else:
            good.append(gp[i])
    ans = []
    for i in bad:
        good.append(i)
    good.sort()
    for i in good:
        for j in range(i[1]):ans.append(i[0])
    print(''.join([str(i) for i in ans]))
