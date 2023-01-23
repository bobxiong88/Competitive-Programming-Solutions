import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
pairs = []
for i in range(1,int(k**0.5)+1):
    if k%i==0:
        pairs.append((i,k//i))
sa = 0
sb = 0
pa = [0]
pb = [0]
for i in range(n):
    sa+=a[i]
    pa.append(sa)
for i in range(m):
    sb+=b[i]
    pb.append(sb)
ans = 0
for fa,fb in pairs:
    c1 = 0
    c2 = 0
    for i in range(n-fa+1):
        if pa[i+fa]-pa[i]==fa:
            c1+=1
    for i in range(m-fb+1):
        if pb[i+fb]-pb[i]==fb:
            c2+=1
    ans+=c1*c2
    c1,c2=0,0
    if fa==fb:
        continue
    for i in range(n-fb+1):
        if pa[i+fb]-pa[i]==fb:
            c1+=1
    for i in range(m-fa+1):
        if pb[i+fa]-pb[i]==fa:
            c2+=1
    ans+=c1*c2
print(ans)
