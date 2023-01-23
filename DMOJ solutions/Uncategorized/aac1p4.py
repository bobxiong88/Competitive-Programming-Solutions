import sys
input = sys.stdin.readline
def find(n, l, r):
    if not freq[n]:
        return False
    tl = 0
    tr = len(freq[n])-1
    if freq[n][tr] < l:
        return False
    if freq[n][tl] > r:
        return False
    while tl <= tr:
        m = (tl+tr)//2
        if l <= freq[n][m] <= r:
            return True
        if freq[n][m] > r:
            tr = m-1
        else:
            tl = m+1
    return False
mx = int(1e5)+5
factor = [[] for i in range(mx)]
for i in range(2, mx):
    for j in range(1, int(i**0.5)+1):
        if i%j == 0:
            if i // j != j:
                factor[i].append((j, i//j))
N, Q = map(int,input().split())
a = list(map(int,input().split()))
freq = [[] for i in range(mx)]
for i in range(N):
    freq[a[i]].append(i+1)
for i in range(Q):
    l, r, x = map(int,input().split())
    ans = "NO"
    for c, d in factor[x]:
        if find(c, l, r) and find(d, l, r):
            ans = "YES"
            break
    print(ans)