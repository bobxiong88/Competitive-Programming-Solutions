import sys
input = sys.stdin.readline
def f(x):
    sz = sum(k)+x
    freq = [0]*(m+1)
    for i in range(sz):
        freq[a[i]] += 1
    small = 0
    for i in range(1,m+1):
        if freq[i] < k[i]:
            small += 1
    if not small: return True
    for i in range(sz, n):
        freq[a[i-sz]] -= 1
        if freq[a[i-sz]] == k[a[i-sz]]-1:
            small += 1
        freq[a[i]] += 1
        if freq[a[i]] == k[a[i]]:
            small -= 1
        if not small: return True
    return False
global n,m
n, m = map(int,input().split())
a = list(map(int,input().split()))
k = [0]+list(map(int,input().split()))
freq = [0]*(m+1)
for i in a:
    freq[i] += 1
for i in range(1,m+1):
    if freq[i] < k[i]:
        print(-1)
        sys.exit(0)
l = 0
r = n-sum(k)
ans = r
while l <= r:
    x = (l+r)//2
    if f(x):
        ans = x
        r = x-1
    else:
        l = x+1
print(ans)
