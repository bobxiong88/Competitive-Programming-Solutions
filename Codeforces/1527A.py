import sys
input = sys.stdin.readline
def get (left, right):
    res = 0
    while (left<right):
        left >>= 1
        right >>= 1
        res +=1
    res = right << res;
    return res
for _ in range(int(input())):
    n = int(input())
    l = 0
    r = n
    ans = 0
    while (l<=r):
        m = (l+r)//2
        if get(m, n) == 0:
            l = m+1
            ans = max(ans, m)
        else:
            r = m-1
    print(ans)
