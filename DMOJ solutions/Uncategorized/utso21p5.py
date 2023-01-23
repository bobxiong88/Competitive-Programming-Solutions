import sys
input = sys.stdin.readline
def update(index, value, tree):
    while index < Q+1:
        tree[index] += value
        index += index & -index
def get_sum(index, tree):
    ans = 0
    while index > 0:
        ans += tree[index]
        index -= index& -index
    return ans
N, Q = map(int,input().split())
val = [0]+list(map(int,input().split()))
upd = [[] for i in range(N+2)]
qry = [[] for i in range(N+2)]
for i in range(Q):
    i = i+1
    query = list(map(int,input().split()))
    if query[0] == 1:
        l, r, x = query[1:]
        upd[l].append((x, i))
        upd[r+1].append((-x, i))
    else:
        l, r = query[1:]
        qry[l].append((1, i))
        qry[r+1].append((-1, i))
ans = [0]*(N+1)
cnt = 0
tot = 0
ts = [0]*(Q+1)
tc = [0]*(Q+1)
for p in range(1,N+1):
    for x, i in upd[p]:
        update(i, x, ts)
        tot += (cnt-get_sum(i-1,tc))*x
    for t, i in qry[p]:
        update(i, t, tc)
        cnt += t
        tot += get_sum(i, ts)*t
    ans[p] = tot+cnt*val[p]
print(' '.join([str(i) for i in ans[1:]]))