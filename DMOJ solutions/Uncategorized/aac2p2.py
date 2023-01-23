import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
s = set()
for i in a:
    s.add(i)
ans = 1
if N>2: ans = 2
for i in range(N):
    for j in range(i+1,N):
        if (a[i]+a[j])%2==0:
            res = 2
            if (a[i]+a[j])//2 in s:
                res+=1
            ans = max(ans, res)
            if ans == 3:
                break
    if ans == 3:
        break
print(ans)