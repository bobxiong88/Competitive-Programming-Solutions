#already solved this problem, just testing
import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
a = [0]+list(map(int,input().split()))
i = 1
j = 1
seg = []
cnt = [0]*(N+1)
while j <= N:
    while j <= N and (not cnt[a[j]]):
        cnt[a[j]]=1
        j+=1
    seg.append((i, j-1))
    while j<=N and cnt[a[j]]:
        cnt[a[i]]=0
        i+=1
ans = 0
for i in range(Q):
    l, r = map(int,input().split())
    l^=ans
    r^=ans
    ans = 0
    for a, b in seg:
        if a <= l and r <= b:
            ans = max(ans, b-a+1)
    print(ans)