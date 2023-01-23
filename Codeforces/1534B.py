import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = [0]+list(map(int,input().split()))+[0]
    ans = 0
    for i in range(1,n+1):
        og = a[i]
        if a[i] > a[i-1] and a[i] > a[i+1]:
            a[i] = max(a[i+1],a[i-1])
            ans += og-a[i]
    for i in range(1,n+2):
        ans += abs(a[i]-a[i-1])
    print(ans)
