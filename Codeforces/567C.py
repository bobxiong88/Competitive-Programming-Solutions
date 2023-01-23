import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
left = dict()
right = dict()
for i in range(n):
    if a[i] in right:
        right[a[i]]+=1
    else:
        right.update({a[i]:1})
        left.update({a[i]:0})
ans = 0
for i in range(n):
    right[a[i]]-=1
    if not a[i]%k:
        if a[i]//k in left and a[i]*k in right:
            ans += left[a[i]//k]*right[a[i]*k]
    left[a[i]]+=1
print(ans)
