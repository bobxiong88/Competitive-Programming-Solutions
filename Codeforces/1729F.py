import sys
input = sys.stdin.readline
def build(n):
    for i in range(n-1, 0, -1): t[i] = (t[i<<1]+t[i<<1|1])%9
def update(p, value, n):
    p+=n
    t[p] = value
    while p>1:
        t[p>>1] = (t[p] + t[p^1])%9
        p>>=1
def query(l, r, n):
    r+=1
    res = 0
    l+=n
    r+=n
    while l<r:
        if l&1:
            res += t[l]
            l+=1
        if r&1:
            r-=1
            res += t[r]
        r>>=1
        l>>=1
    return res%9

for _ in range(int(input())):
    s = [0]+[int(i) for i in list(input().strip())]
    n = len(s)
    t = [0]*(2*n+2)
    for i in range(n):
        t[n+i] = s[i]
    build(n)
    w, m = map(int,input().split())
    mod = [[] for i in range(9)]
    for i in range(1,n-w+1):
        mod[query(i,i+w-1,n)].append(i)
    for i in range(m):
        l,r,k = map(int,input().split())
        x = query(l,r,n)
        a = -1
        b = -1
        pos = []
        for i in range(9):
            if mod[i]:
                for j in range(9):
                    if mod[j]:
                        if (i*x+j)%9 == k:
                            if i == j:
                                if len(mod[i])>1:
                                    pos.append((mod[i][0],mod[i][1]))
                            else:
                                pos.append((mod[i][0],mod[j][0]))
        if len(pos):
            a,b = min(pos)
        #res = query(a,a+w-1,n)*x+query(b,b+w-1,n)
        print(a,b)
