import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    aa = list(input())[:n]
    bb = list(input())[:n]
    a = []
    b = []
    p = True
    array = [[] for i in range(20)]
    for i in range(n):
        if aa[i]==bb[i]: continue
        a.append(ord(aa[i]))
        b.append(ord(bb[i]))
        if a[-1]>b[-1]:
            p = False
            break
        array[a[-1]-97].append(b[-1]-a[-1])
    if not p:
        print(-1)
        continue
    ans = 0
    for i in range(20):
        if not array[i]: continue
        s = min(array[i])
        ans+=1
        for j in set(array[i]):
            if j == s: continue
            array[i+s].append(j-s)
    print(ans)
