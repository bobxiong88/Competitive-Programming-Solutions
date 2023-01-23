import sys
input = sys.stdin.readline
N = int(input())
l = 1
r = int(1e9)
ans = int(1e9)
while l<=r:
    m = (l+r)//2
    if m%2 == 0:
        x = (m+1)*(m//2)+(m//2)+1
    else:
        x = (m+1)*(m//2+1)
    if x >= N:
        r = m-1
        ans = min(m, ans)
    else:
        l = m+1
print(ans)