import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    o = []
    e = []
    for i in a:
        if i%2: o.append(i)
        else: e.append(i)
    ans = False
    if len(o)%2 and len(e)%2:
        for i in o:
            for j in e:
                if i==j+1 or i==j-1:
                    ans = True
    else:
        ans = True
    if ans: print('YES')
    else: print('NO')
        
