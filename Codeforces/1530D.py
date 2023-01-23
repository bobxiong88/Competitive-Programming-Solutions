import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    g = [[] for i in range(n)]
    rg = [[] for i in range(n)]
    
    for i in range(n):
        a[i] -= 1
        g[i].append(a[i])
        rg[a[i]].append(i)
    imp = a[:]
    # make node with at least 1 parent always have one parent
    nop = []
    gp = []
    for i in range(n):
        if not rg[i]:
            nop.append(i)
        if len(rg[i]) > 1:
            gp.append(rg[i])
    
    if len(nop) == 0:
        for i in range(n): a[i] += 1
        print(n)
        print(*a)
    elif len(nop) == 1:
        for i in gp[0]:
            if i != nop[0]:
                imp[i] = nop[0]
                break
        ans = 0
        for i in range(n):
            a[i] += 1
            imp[i] += 1
            if imp[i] == a[i]: ans += 1
        print(ans)
        print(*imp)
    else:
        b = []
        for i in gp:
            for j in i:
                if j != i[-1]:
                    b.append(j)
        nop.sort()
        b.sort()
        for i in range(len(nop)):
            if nop[i] == b[i]:
                b[i], b[i-1] = b[i-1], b[i]
        for i in range(len(nop)):
            imp[b[i]] = nop[i]
        ans = 0
        for i in range(n):
            a[i] += 1
            imp[i] += 1
            if imp[i] == a[i]: ans += 1
        print(ans)
        print(*imp)
