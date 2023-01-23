import sys
input = sys.stdin.readline
def search():
    v = s-W
    l = 0
    r = len(a)-1
    if v<=0: return 1
    while l<=r:
        m = (l+r)//2
        if prep[m-1] < v <= prep[m]: return m+1
        elif prep[m] > v: r = m-1
        else: l = m+1
N, W = map(int,input().split())
a = [(0,0)]
prep = [0]
prec = [0]
dp = [0 for i in range(N+1)]
s = 0
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'A':
        p, c = map(int,cmd[1:])
        s += p
        a.append((p,c))
        prep.append(prep[-1]+p)
        prec.append(prec[-1]+c)
        r = len(a)-1
        l = search()
        if l>r: res = 0
        else: res = prec[r]-prec[l-1]
        dp[r] = max(dp[r-1], res)
        print(dp[r])
    else:
        s -= a.pop()[0]
        prep.pop()
        prec.pop()
        dp.pop()