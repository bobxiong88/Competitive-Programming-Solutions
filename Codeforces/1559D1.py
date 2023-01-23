import sys
input = sys.stdin.readline
def find(i, v):
    if v == par[i][v]: return v
    par[i][v] = find(i,par[i][v])
    return par[i][v]
def join(i, u, v):
    u = find(i, u)
    v = find(i, v)
    if u == v: return
    if sz[i][u] < sz[i][v]: u, v = v , u
    par[i][v] = u
    sz[i][u] += sz[i][v]
n,m1,m2 = map(int,input().split())
par = [[i for i in range(n+1)] for j in range(2)]
sz = [[1 for i in range(n+1)] for j in range(2)]
for i in range(m1):
    u, v = map(int,input().split())
    join(0, u, v)
for i in range(m2):
    u, v = map(int,input().split())
    join(1, u, v)
ans = []
for _ in range(n):
    comp = [[] for j in range(n+1)]
    for j in range(1,n+1):
        comp[find(0, j)].append((find(1, j), j))
    rem = []
    for j in range(1,n+1):
        if comp[j]:
            comp[j].sort()
            gay = []
            for i in range(len(comp[j])):
                if i == 0:
                    gay.append(comp[j][i])
                else:
                    if comp[j][i][0] != comp[j][i-1][0]:
                        gay.append(comp[j][i])
            rem.append(gay)
            #print(j, comp[j])
    st = []
    no = []
    for gay in rem:
        if len(gay) >=2 and not st:
            st = gay
        else:
            no.append(gay[0])
    if st:
        found = False
        for a, b in st:
            for u, v in no:
                if a != u:
                    ans.append((b, v))
                    join(0, b, v)
                    join(1, b, v)
                    found = True
                    break
            if found: break
    else:
        no.sort()
        found = False
        for i in range(len(no)-1):
            if no[i][0] != no[i+1][0]:
                ans.append((no[i][1], no[i+1][1]))
                join(0, no[i][1], no[i+1][1])
                join(1, no[i][1], no[i+1][1])
                found = True
                break
    if not found: break
print(len(ans))
for u, v in ans:
    print(u,v)
