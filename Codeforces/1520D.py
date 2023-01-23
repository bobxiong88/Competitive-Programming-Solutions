import sys
input = sys.stdin.readline
for _ in range(int(input())):
    ans = 0
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0]*(2*n+2)
    for i in range(n):
        ans += cnt[a[i]-i]
        cnt[a[i]-i] += 1
    print(ans)
