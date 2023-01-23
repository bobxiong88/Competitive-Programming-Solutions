import sys
input = sys.stdin.readline
def check(x, s):
    n = len(a)
    cum = sum(a[:x])
    if cum <= s: return True
    for i in range(x, n):
        cum += a[i]
        cum -= a[i-x]
        if cum <= s: return True
    return False
for _ in range(int(input())):
    n, s = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a) < s:
        print(-1)
        continue
    l = 0
    r = n
    ans = 0
    while l <= r:
        m = (l+r)//2
        if check(m, s):
            ans = m
            l = m+1
        else:
            r = m-1
    print(n-ans)
